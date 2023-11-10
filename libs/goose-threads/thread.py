from pydantic import BaseModel
from typing import Protocol


class Message(BaseModel):
    content: str


class ThreadListener(Protocol):
    def get_listener_id() -> str:
        pass

    def on_thread_push():
        pass

    def equals(other: "ThreadListener") -> bool:
        pass


class Thread(BaseModel):
    messages: list[Message]
    listeners: list[ThreadListener]

    def push(self, msg: Message):
        for listener in self.listeners:
            listener.on_thread_push()
        self.messages.append(msg)

    def register(self, listener: ThreadListener):
        self.listeners.append(listener)

    def unregister(self, listener: ThreadListener):
        self.listeners = [
            thread_listener
            for thread_listener in self.listeners
            if thread_listener.equals(listener)
        ]
