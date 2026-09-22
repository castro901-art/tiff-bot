"""Execution boundary for Super Computer capabilities."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionRequest:
    """A normalized request that can be handed to an execution adapter."""

    action: str
    payload: dict[str, object]


class SuperComputer:
    """Placeholder for Browse, Code, Run, Files, Websites, and Build & Test."""

    def submit(self, request: ExecutionRequest) -> str:
        """Return a stable placeholder until a real executor is connected."""
        if not request.action.strip():
            raise ValueError("request action must not be empty")
        return f"queued:{request.action}"
