# Multi-Source Research Agent

A multi-agent AI pipeline that takes a research question, searches Wikipedia and arXiv, and synthesizes a cited summary. Built out of frustration with manually aggregating sources during ML coursework.

## How it works
```
Question
   │
   ▼
[Planner Agent]       ← breaks question into focused sub-queries
   │
   ▼
[Search Agent]        ← hits Wikipedia API + arXiv API per sub-query
   │
   ▼
[Synthesis Agent]     ← writes a cited summary using only retrieved sources
   │
   ▼
Research Report (summary + citations + audit trace)
```

## Patterns demonstrated

| Pattern | Implementation |
|---|---|
| Multi-step orchestration | Planner → Search → Synthesis, sequenced by orchestrator |
| Agent-to-agent handoff | Typed Pydantic models enforce contracts between agents |
| Tool use | Agents call real external APIs (Wikipedia REST, arXiv Atom) |
| Source grounding | Synthesis agent cites only retrieved sources — no hallucinated references |
| Audit tracing | Every agent logs start/complete with timestamps |

## Setup
```bash
git clone https://github.com/NusratAfrin/multi-source-research-agent.git
cd multi-source-research-agent
python -m venv venv
source venv/Scripts/activate        # Windows Git Bash
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key_here" > .env
```

Get a free API key at [console.groq.com](https://console.groq.com).

## Run
```bash
python demo.py
```
