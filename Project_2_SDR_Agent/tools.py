from agents import function_tool
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from typing import Dict



@function_tool
def send_email(body: str, recipient: str = "maloderameshwar39@gmail.com"):
    """Send the finalized cold sales email selected by the Sales Manager agent. 
    this tool should only be called after all candidate emails are generated and evaluated.
    Deliver the email exactly as provided to the intended recipient"""
    
    sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("rameshwarpmalode@gmail.com")  
    to_email = To(recipient)       
    content = Content("text/plain", body)
    
    mail = Mail(from_email, to_email, "Sales email", content)
    response = sg.client.mail.send.post(request_body=mail.get())
    
    return {"status": "success", "response_code": response.status_code}

@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to all sales prospects."""
    sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("rameshwarpmalode@gmail.com")  
    to_email = To("maloderameshwar39@gmail.com")       
    content = Content("text/html", html_body)

    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)

    return {"status": "success", "response_code": response.status_code}