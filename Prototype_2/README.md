# Agent_IDE — AI Filesystem Coding Agent

An autonomous AI agent powered by **Groq + Meta-LLaMA-3.1-8B-Instant** that can **create folders, generate code, and write files on your local machine** — similar to modern AI IDEs like Antigravity, Cursor, and Devin.

The LLM never touches the OS directly.  
It only outputs **structured instructions** that are executed by safe Python tools.

```
Agent_IDE/
│
├── agent.py → The AI agent engine (planner + executor)
├── llm.py → Groq + LLaMA model interface
├── tools.py → Sandboxed filesystem tools
├── .gitignore → Prevents secrets & generated files from being pushed
└── workspace/ → AI-generated project output (ignored by Git)
```
