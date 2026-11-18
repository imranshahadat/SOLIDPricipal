from dataclasses import dataclass


@dataclass
class Money:
    send: int
    desc: str
