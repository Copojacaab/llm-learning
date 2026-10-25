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

- [Ollama docs: Modelfile parameters](https://docs.ollama.com/modelfile)
  Table of generation parameters with defaults (temperature 0.8, seed, top_k, top_p, num_ctx, num_predict). Use for: what each `options` key does.
- [Ollama docs: FAQ](https://docs.ollama.com/faq)
  How long models stay in memory (5 minutes), `keep_alive`, `OLLAMA_KEEP_ALIVE`, `ollama stop`. Use for: load time and memory questions.
- [Ollama docs: Streaming](https://docs.ollama.com/capabilities/streaming)
  What streaming is, and that chunks must be accumulated to keep the conversation history. Use for: streaming with chat, thinking, tools.
- [Hugging Face blog: How to generate text (Patrick von Platen, 2020)](https://huggingface.co/blog/how-to-generate)
  Clear explanation of greedy decoding, sampling, temperature, top-k, top-p, with pictures. Use for: the mechanism behind `temperature`.
- [Ollama docs: Structured outputs](https://docs.ollama.com/capabilities/structured-outputs)
  The `format` field: JSON mode and JSON schema, Pydantic example, tips (temperature 0, schema also in the prompt). Use for: every extraction task.
- [Pydantic docs: Models](https://docs.pydantic.dev/latest/concepts/models/)
  `BaseModel`, `model_json_schema()`, `model_validate_json()`, `model_dump_json()`. Use for: defining the fields to extract and checking the output.
- [Hamel Husain: Your AI Product Needs Evals (2024)](https://hamel.dev/blog/posts/evals/)
  Practitioner guide: three levels (unit tests/assertions, human and model review of traces, A/B tests), "look at your data". Use for: designing every eval, from the invoice extractor to the briefing.
- [Python tutorial: keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
  `*args` / `**kwargs` in definitions and calls. Use for: passing `options` through helper functions.

## Wisdom (Communities)

_None yet. Optional: find one when the first real agent exists (candidate: r/LocalLLaMA, check moderation quality first)._

## Gaps

- A high-trust source on tool use / agent loops with small local models.
- A source on PDF extraction for invoices.
