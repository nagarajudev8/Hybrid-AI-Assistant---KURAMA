🦊 KURAMA

Enterprise-Grade Hybrid AI Assistant
Built with DevOps principles. Designed for intelligence, reliability, and control.

Inspired by the Nine-Tailed Fox — powerful, controlled, and engineered.

🧠 Overview

KURAMA is a modular hybrid AI assistant framework designed with production-grade architecture and DevOps best practices.

It combines:

Local-first AI processing using Ollama
Secure system command orchestration
REST API interface (FastAPI)
Containerized deployment
CI/CD-ready architecture
Extensible cloud intelligence (future support for providers like OpenAI)

KURAMA is not just a chatbot — it is an AI system engineered with infrastructure discipline.

🏗 Architecture

KURAMA follows a modular layered architecture:

User Input
    ↓
Intent Classification Layer
    ↓
Decision Engine (Routing)
   ↙                     ↘
Local LLM             Command Executor
(Ollama)              (Validated & Secure)
    ↓
Response Formatter
    ↓
API Output

Design Principles

🔐 Security-first command validation
🧠 Intent-driven routing logic
⚙️ Modular service separation
📦 Containerized runtime
📊 Observability-ready structure
☁️ Hybrid-ready (Local + Cloud extensibility)


📁 Project Structure

kurama/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── core/
│   ├── chakra_engine.py     # Routing logic (formerly brain)
│   ├── sharingan.py         # Intent classifier
│   └── memory.py
│
├── llm/
│   └── ollama_client.py
│
├── commands/
│   ├── executor.py
│   └── allowed_commands.py
│
├── utils/
│   └── logger.py
│
└── .github/workflows/
        ci.yml
```bash
kurama/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── core/
│   ├── chakra_engine.py
│   ├── sharingan.py
│   └── memory.py
│
├── llm/
│   └── ollama_client.py
│
├── commands/
│   ├── executor.py
│   └── allowed_commands.py
│
├── utils/
│   └── logger.py
│
└── .github/
    └── workflows/
        └── ci.yml

⚙️ Core Capabilities (Phase 1)

Local LLM inference via Ollama
Secure system command execution layer
FastAPI REST interface
Dockerized deployment
CI pipeline integration
Structured modular backend
