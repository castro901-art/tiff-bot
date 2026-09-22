"""Send a message to the Tiffbot chat endpoint.

Usage:
    python examples/chat.py "Help me plan the next move"
"""

from __future__ import annotations

import json
import sys
from urllib.request import Request, urlopen


API_URL = "http://localhost:8000"


def main() -> None:
    message = " ".join(sys.argv[1:]).strip() or "What can you help me build?"
    request = Request(
        f"{API_URL}/chat",
        data=json.dumps({"message": message}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        print(json.dumps(json.loads(response.read()), indent=2))


if __name__ == "__main__":
    main()
