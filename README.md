# UMI Provider Gateway

UMI Provider Gateway is a self-hosted multi-provider AI routing architecture designed for AI-assisted development workflows, agent orchestration, and local AI infrastructure experimentation.

## Core Features

- Unified AI gateway
- Multi-provider routing
- Quota-aware orchestration
- Streaming-ready architecture
- Provider abstraction layer
- Local encrypted session storage
- FastAPI backend
- Agent-oriented workflow design

## Supported Providers

- UMI-Kiro
- UMI-Canva
- UMI-Wavespeed
- UMI-CodeBuddy
- UMI-YepAPI

## Architecture

```text
User/UI
↓
UMI Gateway API
↓
Provider Router
↓
Provider Adapter Layer
├── UMI-Kiro
├── UMI-Canva
├── UMI-Wavespeed
├── UMI-CodeBuddy
└── UMI-YepAPI
↓
Encrypted Session Manager
↓
Official AI APIs
```

## Use Cases

- AI coding workflows
- Multi-agent orchestration
- Backend automation
- AI infrastructure prototyping
- Local AI gateway experimentation
- Provider balancing & routing

## Quick Start

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

Open:
http://127.0.0.1:8000/docs

## Disclaimer

Educational self-hosted gateway prototype using official API patterns and local-only architecture.