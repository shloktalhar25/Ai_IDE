# Golang Tooling Layer for Secure AI Agents

This project implements a **secure tool execution layer written in Golang** that sits between an LLM-powered agent (Python) and the real operating system.

It solves the core problem in modern **AI IDEs, autonomous agents, and coding copilots**:

> **How can we let an LLM create files, build projects, and run code without risking the host OS?**

The answer is **capability-based security using a Go tool server**.

---

## Problem 

LLMs are now used as autonomous coding agents that:
- Create folders
- Write source code
- Modify projects
- Run builds and tests

But giving an LLM **direct access to Python’s `os`, `open()`, or `subprocess`** is extremely dangerous.

A single hallucination or prompt injection can cause:
- File deletion
- Credential leaks
- Ransomware-like behavior
- OS corruption

This is not theoretical — it has happened in real agent frameworks.

## Solution

We separate **thinking** from **doing**.

LLM → Python Agent → JSON → Golang Tool Server → Workspace

- Python only plans and sends structured JSON.
- Golang is the only layer that touches the filesystem.
- The LLM never sees the real OS.

---

##  Why Golang?

Golang is:
- Compiled
- Fixed at runtime
- Not dynamically modifiable

This means the LLM cannot:
- Inject code
- Import new powers
- Escape the sandbox

Only the tools defined in Go exist.
