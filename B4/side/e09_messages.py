# Step 09, on the side: one abstract family, three kinds, no "if kind ==".
# Run from the track folder: uv run python B4/side/e09_messages.py

from abc import ABC, abstractmethod


class Message(ABC):
    """What every message has. Message itself cannot be created."""

    kind = "message"  # each subclass replaces it

    def __init__(self, recipient: str, text: str) -> None:
        if text.strip() == "":
            raise ValueError("A message needs a text.")
        self.recipient = recipient
        self.text = text

    @abstractmethod
    def cost(self) -> float:
        """Each kind must say how much it costs."""

    def summary(self) -> str:
        # Written once, here: it calls cost(), whichever kind self is.
        return f"{self.kind} to {self.recipient}: {self.cost():.2f} EUR"


class Email(Message):
    kind = "email"

    def cost(self) -> float:
        return 0.0


class Sms(Message):
    kind = "sms"

    def cost(self) -> float:
        parts = (len(self.text) - 1) // 160 + 1  # 160 characters per SMS
        return 0.08 * parts


class Letter(Message):
    kind = "letter"

    def __init__(self, recipient: str, text: str, registered: bool = False) -> None:
        super().__init__(recipient, text)  # the common part, then its own
        self.registered = registered

    def cost(self) -> float:
        return 5.36 if self.registered else 1.39


# From data: the "kind" field chooses the class, in one place only.
KINDS = {"email": Email, "sms": Sms, "letter": Letter}


def message_from_dict(data: dict) -> Message:
    if data["kind"] not in KINDS:
        raise ValueError(f"Unknown kind {data['kind']!r}.")
    message_class = KINDS[data["kind"]]
    options = dict(data)
    del options["kind"]
    return message_class(**options)  # ** passes the dict as named arguments


outbox = [
    message_from_dict({"kind": "email", "recipient": "lou@example.org", "text": "Hi"}),
    message_from_dict({"kind": "sms", "recipient": "06 12", "text": "x" * 200}),
    message_from_dict(
        {"kind": "letter", "recipient": "M. Diallo", "text": "...", "registered": True}
    ),
]
total = 0.0
for message in outbox:
    print(message.summary())  # each object answers with its own cost()
    total += message.cost()
print(f"Total: {total:.2f} EUR")

try:
    Message("someone", "hello")
except TypeError as error:
    print(f"Refused: {error}")
