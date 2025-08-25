from agents import Agent, Runner, trace, input_guardrail, GuardrailFunctionOutput
from .prompt import (
    Instruction1,
    Instruction2,
    Instruction3,
    Instruction4,
    Instruction5,
    subject_instructions,
    html_instructions,
)
from .tools import send_email, send_html_email
from pydantic import BaseModel


#Sales Agents 
sales_agent1 = Agent(name="Direct & Concise Pitch sales agent", instructions=Instruction1, model="gpt-4o-mini")
sales_agent2 = Agent(name="Problem–Solution Storytelling sales agent", instructions=Instruction2, model="gpt-4o-mini")
sales_agent3 = Agent(name="Relationship-Focused, Warm Intro agent", instructions=Instruction3, model="gpt-4o-mini")

tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description="Write a cold sales email")
tool2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description="Write a cold sales email")
tool3 = sales_agent3.as_tool(tool_name="sales_agent3", tool_description="Write a cold sales email")

tools = [tool1, tool2, tool3]


# Subject and HTML Agents
subject_writer = Agent(name="Email subject writer", instructions=subject_instructions, model="gpt-4o-mini")
subject_tool = subject_writer.as_tool(tool_name="subject_writer", tool_description="Write a subject for a cold sales email")

html_converter = Agent(name="HTML email body converter", instructions=html_instructions, model="gpt-4o-mini")
html_tool = html_converter.as_tool(tool_name="html_converter", tool_description="Convert a text email body to an HTML email body")


# Email Manager Agent (handoff target)
email_tools = [subject_tool, html_tool, send_html_email]

emailer_agent = Agent(
    name="Email Manager",
    instructions=Instruction5,
    tools=email_tools,
    model="gpt-4o-mini",
    handoff_description="Convert an email to HTML and send it",
)

# # Sale manager agent
# sales_manager = Agent(
#     name="Sales Manager",
#     instructions=Instruction4,
#     tools=tools,
#     handoffs=[emailer_agent],
#     model="gpt-4o-mini",
# )

# Guardrail Agent 
class NameCheckOutput(BaseModel):
    is_name_in_message: bool
    name: str


guardrail_agent = Agent(
    name="Name check",
    instructions="Check if the user is including someone's personal name in what they want you to do.",
    output_type=NameCheckOutput,
    model="gpt-4o-mini",
)



@input_guardrail
async def guardrail_against_name(ctx, agent, message):
    result = await Runner.run(guardrail_agent, message, context=ctx.context)
    is_name_in_message = result.final_output.is_name_in_message
    return GuardrailFunctionOutput(
        output_info={"found_name": result.final_output},
        tripwire_triggered=is_name_in_message,
    )


careful_sales_manager = Agent(
    name="Sales Manager (Guarded)",
    instructions=Instruction4,
    tools=tools,
    handoffs=[emailer_agent],
    model="gpt-4o-mini",
    input_guardrails=[guardrail_against_name],
)


#Runner 
async def run_sales_manager():
    message = "Send a cold sales email addressed to 'Dear CEO'"
    with trace("Sales manager"):
        result = await Runner.run(careful_sales_manager, message)
    return result
