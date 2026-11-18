from abc import ABC,abstractmethod
from dataclasses import dataclass


@dataclass
class MessageClass:
    send:str
    typeof:str


class InterfaceDIP(ABC):
    @abstractmethod
    def sendmsg(self,msg:MessageClass):
        pass  

class EmailClass(InterfaceDIP):
    def sendmsg(self, msg: MessageClass):
        print(f"this message send by the email class {msg.send} ")
        print(f"this message send by the email class {msg.typeof} ")


class SMSClass(InterfaceDIP):
    def sendmsg(self, msg: MessageClass):
        print(f"this message send by the SMS class {msg.send} ")
        print(f"this message send by the SMS class {msg.typeof} ")



        # ////////////////


class ServiceOrchannelclass:
    def __init__(self,channel:InterfaceDIP) -> None:
        self.channel = channel
    def MainService(self,msg:MessageClass):
        self.channel.sendmsg(msg)


sms = SMSClass()
mail= EmailClass()
service = ServiceOrchannelclass(sms)
# service.MainService("msg")

