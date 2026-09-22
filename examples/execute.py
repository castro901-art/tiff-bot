"""Queue a Super Computer action through the Tiffbot API.

Usage:
    python examples/execute.py code
"""

from __future__ import annotations

import json
import sys
from urllib.request import Request, urlopen


API_URL = "http://localhost:8000"


def main() -> None:
    action = (sys.argv[1] if len(sys.argv) > 1 else "code").strip()
    payload = {"intent": "example execution request", "source": "examples/execute.py"}
    request = Request(
        f"{API_URL}/execute",
        data=json.dumps({"action": action, "payload": payload}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        print(json.dumps(json.loads(response.read()), indent=2))


if __name__ == "__main__":
    main()
