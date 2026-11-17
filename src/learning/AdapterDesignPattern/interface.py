from abc import ABC,abstractmethod


class MainClass(ABC):
    @abstractmethod
    def Send(self, to: str, subject: str, cc: str):
        pass

    @abstractmethod
    def Recive(self, sender: str, subject: str, cc: str):
        pass


class Emailsender(MainClass):
    def Send(self, to: str, subject: str, cc: str):
        print(f"this mail to {to} and subject is {subject} and cc is {cc}")

    def Recive(self, sender: str, subject: str, cc: str):
        print(f"this mail to {sender} and subject is {subject} and cc is {cc}")


# Different service 
class SendsendgridmailService:
    def sender(self, whichone: str, subject: str, content: str):
        print(f"this sendgrid mail to {whichone} and subject is {subject} and content is {content}")

    def receiver(self, sender: str, subject: str, content: str):
        print(f"this sendgrid receive from {sender} with subject {subject} and content is {content}")

class AdapeterClass(MainClass):
    def __init__(self, sendGridSerive: SendsendgridmailService):
        self.sendGridSerive = sendGridSerive

    def Send(self, to: str, subject: str, cc: str):
            
        # Adapt MainClass's Send method to SendGrid's sender method
        self.sendGridSerive.sender(to, subject, cc)
    def Recive(self, sender: str, subject: str, cc: str):  # Fixed: Added missing abstract method
        # Adapt MainClass's Recive method to SendGrid's receiver method (if available)
        self.sendGridSerive.receiver(sender, subject, cc)    


print("--- Using Normal Email ---")
normal_mail: MainClass = Emailsender()
normal_mail.Send("user@example.com", "Welcome", "admin@example.com")

print("\n--- Using SendGrid via Adapter ---")
# Using SendGrid via Adapter
sendgrid_service = SendsendgridmailService()
sendgrid_adapter: MainClass = AdapeterClass(sendgrid_service)
sendgrid_adapter.Send("user@example.com", "Welcome via SendGrid", "admin@example.com")