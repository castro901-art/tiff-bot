# Tiffbot - The Core AI Assistant

> The conversational intelligence layer of Tiff, with integrated Super Computer execution capabilities.

[![Status](https://img.shields.io/badge/status-foundation-7c3aed.svg)](https://github.com/castro901-art/tiff-bot)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776ab.svg)](https://www.python.org/)
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

The default conversational interface for questions, planning, explanation, and direct assistance. Simple questions should receive simple answers without unnecessary execution UI.

The chat layer is responsible for:

- Understanding user intent and context
- Maintaining a coherent conversation
- Answering directly when no external capability is needed
- Routing action-oriented requests to the appropriate capability

### Research

The evidence-gathering layer for questions that require current or external information. Research can search the web, gather relevant sources, and return synthesized answers with traceable citations.

Research should be activated when the answer depends on information outside the conversation or on facts that may have changed.

### Images

The visual generation layer for creating images from natural-language intent. Image requests should feel like a natural continuation of the conversation rather than a separate mode or product surface.

### Super Computer

The execution layer that allows Tiffbot to move from conversation to action. It is activated automatically when a request requires real work in an environment.

The initial execution surface is designed around:

| Capability | Purpose |
| --- | --- |
| Browse | Navigate and interact with web resources |
| Code | Write and inspect software or scripts |
| Run | Execute commands and workloads |
| Files | Create, read, transform, and organize files |
| Websites | Build and work with frontend experiences |
| Build & Test | Validate outputs and iterate toward a working result |

Super Computer is not a separate assistant. It is the capability layer that gives Tiffbot the ability to complete tasks instead of only describing how they could be done.

## Design Principles

1. **One continuous thread** - Conversation, research, images, and execution belong to the same user journey.
2. **Autonomous capability selection** - Tiffbot decides what the request needs; users should not have to manage tools.
3. **Answer before interface** - A simple question gets a direct answer, without exposing unnecessary machinery.
4. **Action when action is required** - Requests involving code, files, browsing, or builds activate Super Computer inline.
5. **Evidence when facts matter** - Research should favor current sources and make the basis of an answer clear.
6. **Execution with verification** - Work is not complete until its output can be checked.

## Project Structure

```text
.
├── src/
│   ├── tiffbot/                 # Core conversational assistant logic
│   │   ├── __init__.py
│   │   └── core.py
│   └── supercomputer/           # Execution layer boundary and adapters
│       ├── __init__.py
│       └── executor.py
├── tests/                       # Deterministic tests for core behavior
│   └── test_smoke.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Getting Started

```bash
git clone https://github.com/castro901-art/tiff-bot.git
cd tiff-bot

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

PYTHONPATH=src pytest
```

The repository is intentionally lightweight at this stage. Runtime integrations and provider-specific dependencies will be added behind the Tiffbot and Super Computer boundaries as the foundation evolves.

## Status

This is the initial open-source foundation for Tiffbot. The current code defines the core boundaries and a minimal execution interface; production providers, orchestration, research adapters, image generation, and expanded test coverage will be added incrementally.

## License

Tiffbot is released under the [MIT License](LICENSE).

Built under **Trendify**.
