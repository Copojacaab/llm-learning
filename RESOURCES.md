# LLMs for Development and Automation Resources

## Knowledge

- [Ollama docs: Linux install](https://docs.ollama.com/linux)
  Official install steps, systemd service, GPU notes. Use for: installing and checking the local server.
- [Ollama docs: /api/chat](https://docs.ollama.com/api/chat)
  The HTTP API behind everything. Fields: model, messages, stream, options, format, keep_alive, tools; response timing fields (eval_count, eval_duration...). Use for: knowing what the Python library really sends and returns.
- [ollama-python (GitHub README)](https://github.com/ollama/ollama-python)
  Official Python client: chat, streaming, Client(host=...). Use for: all code that calls local models.
- [Ollama model library](https://ollama.com/library)
  Model list with sizes and "tools" tags. Use for: choosing a model that fits 8 GB VRAM.
- [Microsoft Learn: WSL advanced settings (.wslconfig)](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
  Official reference for memory/swap limits in WSL 2. Use for: raising the RAM limit.

## Wisdom (Communities)

_None yet. Optional: find one when the first real agent exists (candidate: r/LocalLLaMA, check moderation quality first)._

## Gaps

- A high-trust source on evals for LLM apps (needed before the first agent).
- A high-trust source on tool use / agent loops with small local models.
- A source on PDF extraction for invoices.
