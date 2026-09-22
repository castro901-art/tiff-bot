"""Core conversational boundary for Tiffbot."""

from dataclasses import dataclass


@dataclass(slots=True)
class Tiffbot:
    """Minimal foundation for the Tiffbot assistant.

    Capability routing will be added here as Chat, Research, Images, and
    Super Computer integrations are implemented.
    """

    name: str = "Tiffbot"

    def respond(self, message: str) -> str:
        """Return a temporary response while the orchestration layer evolves."""
        if not message.strip():
            raise ValueError("message must not be empty")
        return "Tiffbot is ready to help."
