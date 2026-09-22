"""Smoke tests for the Tiffbot foundation."""

import pytest

from supercomputer import ExecutionRequest, SuperComputer
from tiffbot import Tiffbot


def test_tiffbot_rejects_empty_messages() -> None:
    with pytest.raises(ValueError):
        Tiffbot().respond(" ")


def test_supercomputer_queues_execution_requests() -> None:
    request = ExecutionRequest(action="code", payload={"language": "python"})
    assert SuperComputer().submit(request) == "queued:code"
