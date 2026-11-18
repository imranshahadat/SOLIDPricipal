from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Email:
    to: str
    subject: str
    cc: str

class EmailSenderPort(ABC):
    @abstractmethod
    def send(self, email: Email) -> None:
        pass

class EmailReceiverPort(ABC):
    @abstractmethod
    def receive(self, email: Email) -> None:
        pass

class SendWelcomeEmailUseCase:
    def __init__(self, sender: EmailSenderPort):
        self._sender = sender
    def execute(self, to: str, subject: str, cc: str):
        email = Email(to=to, subject=subject, cc=cc)
        self._sender.send(email)

class SMTPAdapter(EmailSenderPort, EmailReceiverPort):
    def send(self, email: Email) -> None:
        print(f"this mail to {email.to} and subject is {email.subject} and cc is {email.cc}")
    def receive(self, email: Email) -> None:
        print(f"this mail from {email.to} and subject is {email.subject} and cc is {email.cc}")

class SendsendgridmailService:      # UNCHANGED — the outside world
    def sender(self, whichone: str, subject: str, content: str):
        print(f"this sendgrid mail to {whichone} and subject is {subject} and content is {content}")
    def receiver(self, sender: str, subject: str, content: str):
        print(f"this sendgrid receive from {sender} with subject {subject} and content is {content}")

class SendGridAdapter(EmailSenderPort, EmailReceiverPort):
    def __init__(self, sendgrid_service: SendsendgridmailService):
        self.sendgrid_service = sendgrid_service
    def send(self, email: Email) -> None:
        self.sendgrid_service.sender(email.to, email.subject, email.cc)
    def receive(self, email: Email) -> None:
        self.sendgrid_service.receiver(email.to, email.subject, email.cc)

class MailgunService:
    """Mailgun's own interface — we can't change it."""
    def deliver(self, recipient: str, heading: str, carbon_copy: str):
        print(f"[Mailgun] delivered to {recipient} | heading: {heading} | cc: {carbon_copy}")


class MailgunAdapter(EmailSenderPort):          # ⬅ plugs into the SAME socket
    def __init__(self, mailgun_service: MailgunService):
        self.mailgun_service = mailgun_service

    def send(self, email: Email) -> None:
        # translation:   our world      ->   mailgun's world
        #   email.to     ->   recipient
        #   email.subject ->  heading
        #   email.cc     ->   carbon_copy
        self.mailgun_service.deliver(email.to, email.subject, email.cc)

class CliController:
    def __init__(self, use_case: SendWelcomeEmailUseCase):
        self._use_case = use_case
    def run(self) -> None:
        self._use_case.execute("user@example.com", "Welcome", "admin@example.com")

if __name__ == "__main__":
    print("--- Using Normal Email ---")
    normal_mail_app = CliController(SendWelcomeEmailUseCase(SMTPAdapter()))
    normal_mail_app.run()

    print("\n--- Using SendGrid via Adapter ---")
    sendgrid_app = CliController(SendWelcomeEmailUseCase(
        SendGridAdapter(SendsendgridmailService())
    ))
    sendgrid_app.run()