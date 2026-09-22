"""FastAPI transport for the Tiffbot conversational boundary."""

from __future__ import annotations

import os
from typing import Any
from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from supercomputer import ExecutionRequest, SuperComputer
from tiffbot import Tiffbot


class ChatRequest(BaseModel):
    """Input accepted by the conversational endpoint."""

    message: str = Field(min_length=1, description="The user's message")
    session_id: str | None = Field(default=None, description="Optional conversation identifier")


class ChatResponse(BaseModel):
    """Normalized conversational response."""

    reply: str
    capability: str = "chat"
    session_id: str


class ExecuteRequest(BaseModel):
    """A request for the Super Computer execution boundary."""

    action: str = Field(min_length=1, description="Execution capability, such as code or browse")
    payload: dict[str, Any] = Field(default_factory=dict)


class ExecuteResponse(BaseModel):
    """Acknowledgement returned by the execution placeholder."""

    status: str
    action: str
    result: str


def _cors_origins() -> list[str]:
    configured = os.getenv("TIFF_CORS_ORIGINS", "http://localhost:5173")
    return [origin.strip() for origin in configured.split(",") if origin.strip()]


app = FastAPI(
    title="Tiffbot API",
    description="The conversational and Super Computer execution boundary for Tiff.",
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_assistant = Tiffbot()
_executor = SuperComputer()


@app.get("/health")
def health() -> dict[str, str]:
    """Return a lightweight readiness response."""

    return {"status": "ok", "service": "tiffbot-api"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Respond to a message through the Tiffbot conversational layer."""

    return ChatResponse(
        reply=_assistant.respond(request.message),
        session_id=request.session_id or str(uuid4()),
    )


@app.post("/execute", response_model=ExecuteResponse)
def execute(request: ExecuteRequest) -> ExecuteResponse:
    """Queue work through the Super Computer placeholder."""

    result = _executor.submit(
        ExecutionRequest(action=request.action, payload=request.payload)
    )
    return ExecuteResponse(status="accepted", action=request.action, result=result)
