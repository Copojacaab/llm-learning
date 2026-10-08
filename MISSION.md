# Mission: Using LLMs for development and automation

## Why
I'm a software developer (Python, C) who can't sustain modern pace without intensive LLM support. I want to use LLMs deliberately as guide and reviewer in my dev workflow, and to build agents that automate personal and company processes, understanding them well enough to judge and measure their output.

## Success looks like
- A personal agent acts as my daily secretary: it runs unattended every morning and produces a briefing, for 2 weeks in a row. Built one function at a time; autonomy grows read-only -> propose-and-confirm -> act on low-risk items.
- An invoice/delivery-note pipeline reads real PDFs, extracts fields and flags anomalies, hitting a measured accuracy threshold on a verified document set.
- I can judge whether a company process is automatable, design the workflow, and ship it with human control where needed.
- Every agent I build has evals, not just a demo.
- My dev pipeline (grill-me -> specs -> ticketing -> implement -> test -> review) is stronger, especially test and review, and for C code where LLMs fail silently.

## Constraints
- I implement code myself in order to learn: LLMs are guide and reviewer, not implementer.
- Hardware: RTX 4060 Laptop (8 GB VRAM), WSL. Budget: 20 EUR/month.
- Priority on local/open models (cost, and understanding/controlling the stack). Claude as fallback or comparison when local is too limiting. Company documents: privacy matters.
- 30-minute lesson, one per day. I never wrote code calling an LLM API.
- Already known: context windows, prompts, tokens, tool use, agents, RAG, MCP (concepts).

## Out of scope
- Training or fine-tuning models.
- Letting the LLM do the implementation of my code.
- Autonomous actions (sending mail, registering invoices) before measured reliability.
