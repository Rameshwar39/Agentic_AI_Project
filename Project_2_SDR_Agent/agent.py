from agents import Agent, Runner, trace
from .prompt import Instruction1, Instruction2, Instruction3, Instruction4
from .tools import send_email

#Sales Agents
sales_agent1 = Agent(name="Direct & Concise Pitch sales agent", instructions=Instruction1, model="gpt-4o-mini")
sales_agent2 = Agent(name="Problem–Solution Storytelling sales agent", instructions=Instruction2, model="gpt-4o-mini")
sales_agent3 = Agent(name="Relationship-Focused, Warm Intro agent", instructions=Instruction3, model="gpt-4o-mini")

#converting Agents to Tools
tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description="Write a cold sales email")
tool2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description="Write a cold sales email")
tool3 = sales_agent3.as_tool(tool_name="sales_agent3", tool_description="Write a cold sales email")


tools = [tool1, tool2, tool3, send_email]

# Sales manager agent
sales_manager = Agent(name="Sales Manager", instructions=Instruction4, tools=tools, model="gpt-4o-mini")

# Async-wrapper to run the Sale Manager..
async def run_sales_manager():
    message = "Send a cold sales email addressed to 'Dear CEO'"
    with trace("Sales manager"):
        result = await Runner.run(sales_manager, message)
    return result
