# Tiffbot - The Core AI Assistant

> The conversational intelligence layer of Tiff, with integrated Super Computer execution capabilities.

[![Status](https://img.shields.io/badge/status-foundation-7c3aed.svg)](https://github.com/castro901-art/tiff-bot)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776ab.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/UI-React%20%2B%20Vite-61dafb.svg)](https://vitejs.dev/)
[![License](https://img.shields.io/badge/license-MIT-22c55e.svg)](LICENSE)

Tiffbot is the core AI assistant layer of **Tiff**, built under the **Trendify** product family. It is the conversational surface that understands what a user wants, chooses the right capability, and activates execution when an answer alone is not enough.

## Architecture

Tiff is organized into three layers:

```text
Tiff
├── Tiffbot
│   ├── Chat
│   ├── Research
│   ├── Images
│   └── Super Computer
│       ├── Browse
│       ├── Code
│       ├── Run
│       ├── Files
│       ├── Websites
│       └── Build & Test
└── TiffTeams
    ├── AI employees
    ├── Roles
    ├── Tools
    ├── Tasks
    └── Execution
```

This repository contains the foundation for **Tiffbot** and its connection to the **Super Computer** execution layer. TiffTeams is the organizational layer that can later coordinate teams of AI employees.

## Mental Model

The product is intentionally expressed as a simple progression:

- **Tiffbot** - “Help me do this.” The individual AI assistant and the conversational layer a user interacts with directly.
- **Super Computer** - “Give Tiffbot the ability to actually do it.” The execution environment that lets Tiffbot browse, write and run code, manage files, build websites, and test outcomes.
- **TiffTeams** - “Create a team of AI employees to do this work.” The organizational layer for roles, tools, tasks, and coordinated execution.

The user should not need to select a tool or toggle a mode. Tiffbot decides whether a request needs a plain response, research, image generation, or Super Computer execution, then keeps the experience in one continuous thread.

## Capabilities

### Chat

The default conversational interface for questions, planning, explanation, and direct assistance. The FastAPI `/chat` endpoint accepts a message and optional session identifier, then returns a normalized response.

### Research

The evidence-gathering layer for questions that require current or external information. Research can search the web, gather relevant sources, and return synthesized answers with traceable citations. The current API keeps this capability behind the conversational boundary so it can be added without changing the frontend contract.

### Images

The visual generation layer for creating images from natural-language intent. Image requests should feel like a natural continuation of the conversation rather than a separate mode or product surface.

### Super Computer

The execution layer that allows Tiffbot to move from conversation to action. The FastAPI `/execute` endpoint currently provides a stable placeholder boundary for actions such as `code`, `browse`, `run`, `files`, `websites`, and `build-test`.

| Capability | Purpose |
| --- | --- |
| Browse | Navigate and interact with web resources |
| Code | Write and inspect software or scripts |
| Run | Execute commands and workloads |
| Files | Create, read, transform, and organize files |
| Websites | Build and work with frontend experiences |
| Build & Test | Validate outputs and iterate toward a working result |

Super Computer is not a separate assistant. It is the capability layer that gives Tiffbot the ability to complete tasks instead of only describing how they could be done.

## Full-Stack Layout

```text
.
├── src/
│   ├── tiffbot/
│   │   ├── api.py                # FastAPI app and HTTP contracts
│   │   ├── __init__.py
│   │   └── core.py               # Conversational assistant boundary
│   └── supercomputer/
│       ├── __init__.py
│       └── executor.py            # Execution request boundary
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # One-thread chat interface
│   │   ├── main.jsx
│   │   └── styles.css             # Dark Syne / DM Sans operator aesthetic
│   ├── package.json
│   ├── Dockerfile
│   └── vite.config.js
├── examples/
│   ├── chat.py                    # Standard-library /chat client
│   ├── execute.py                 # Standard-library /execute client
│   └── README.md
├── tests/
│   ├── test_api.py
│   └── test_smoke.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE
└── README.md
```

## Getting Started

### Option 1: Run the API locally

```bash
git clone https://github.com/castro901-art/tiff-bot.git
cd tiff-bot

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

PYTHONPATH=src uvicorn tiffbot.api:app --reload --port 8000
```

The API is available at `http://localhost:8000`. Interactive OpenAPI documentation is available at `http://localhost:8000/docs`, and readiness can be checked at `http://localhost:8000/health`.

### Option 2: Run the React frontend locally

In a second terminal:

```bash
cd tiff-bot/frontend
npm install
npm run dev
```

Open `http://localhost:5173`. The frontend uses `http://localhost:8000` by default. To point it at another API instance, set `VITE_API_URL` before starting Vite:

```bash
VITE_API_URL=http://localhost:8000 npm run dev
```

The interface follows Tiff's UX principles: one continuous thread, autonomous capability selection, direct answers before machinery, and a clear path from intent to execution.

### Option 3: Run the full stack with Docker Compose

From the repository root:

```bash
docker compose up --build
```

This starts:

| Service | Local address | Role |
| --- | --- | --- |
| `backend` | `http://localhost:8000` | FastAPI assistant and execution API |
| `frontend` | `http://localhost:5173` | React + Vite chat interface |

Stop the stack with `Ctrl+C`, or run `docker compose down` from another terminal.

## API Usage

### Chat

```bash
curl -X POST http://localhost:8000/chat \\
  -H "Content-Type: application/json" \\
  -d '{"message":"Help me plan the next move"}'
```

Example response:

```json
{
  "reply": "Tiffbot is ready to help.",
  "capability": "chat",
  "session_id": "a-generated-session-id"
}
```

Pass the returned `session_id` in later requests to keep the conversation associated with the same thread.

### Super Computer execution placeholder

```bash
curl -X POST http://localhost:8000/execute \\
  -H "Content-Type: application/json" \\
  -d '{"action":"code","payload":{"language":"python"}}'
```

Example response:

```json
{
  "status": "accepted",
  "action": "code",
  "result": "queued:code"
}
```

The placeholder intentionally exposes a stable contract before provider-specific execution adapters are connected.

## Examples

With the API running:

```bash
python examples/chat.py "Summarize the Tiff architecture"
python examples/execute.py code
```

See [`examples/README.md`](examples/README.md) for more detail. Both clients use Python's standard library and do not add an extra dependency.

## Development

Run the backend and core tests from the repository root:

```bash
pip install -r requirements.txt
PYTHONPATH=src pytest
```

The API tests cover the `/chat` and `/execute` response contracts. The frontend can be built independently with:

```bash
cd frontend
npm install
npm run build
```

## Design Principles

1. **One continuous thread** - Conversation, research, images, and execution belong to the same user journey.
2. **Autonomous capability selection** - Tiffbot decides what the request needs; users should not have to manage tools.
3. **Answer before interface** - A simple question gets a direct answer, without exposing unnecessary machinery.
4. **Action when action is required** - Requests involving code, files, browsing, or builds activate Super Computer inline.
5. **Evidence when facts matter** - Research should favor current sources and make the basis of an answer clear.
6. **Execution with verification** - Work is not complete until its output can be checked.

## Status

This is an early full-stack foundation for Tiffbot. The repository now includes a working HTTP boundary, a responsive chat surface, executable API examples, and a Docker Compose development path. Production model providers, research adapters, image generation, and real Super Computer execution adapters remain extension points.

## License

Tiffbot is released under the [MIT License](LICENSE).

Built under **Trendify**.
