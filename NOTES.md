# Notes

- Lessons and references in English. User speaks English but doesn't think in it as natively as in Italian: simple sentences, clear technical terms.
- 30 minutes per lesson, one per day.
- Learn by doing on real cases: track A on his own work, track B (code) in longer weekend blocks.
- Recommend communities for the "wisdom" part (optional).
- Lesson 1: install Ollama (and raise the WSL RAM limit in .wslconfig, currently 7.6 GB visible), call a local model from Python. No ollama/uv installed yet; Python 3.14.
- Local models first; hand-written agent loop; then compare against Claude on the same tasks. Teach output constraints, evals, fallback since 7-8B models are fragile at tool use.
- Use sample/anonymized documents for invoices until the company confirms data rules.
- Secretary v1 = morning briefing only; add one function at a time.
- Code lives in `exercises/` with its venv at `exercises/.venv` (ollama-python 0.6.3). Run scripts from there.
- 2026-10-10: WSL still shows 7.6 GB RAM, so lesson 1 step 0 (.wslconfig) was not applied or did not take effect. Fine for 3B models; ask again before pulling a 7-8B model.
- He reports back in the form `[EXPERIMENTS] ... [Q&A] ...`. Keep giving a clear "what to report" list at the end of each lesson.
- Lessons give a spec plus the new API line, with the full solution hidden in a `<details>` block (he wants to write the code himself). Lesson 1 gave full code to type; from lesson 2 on, spec first.
- Before publishing a lesson, run its exercise on his machine with `exercises/.venv/bin/python` to check the numbers.
- 2026-10-13: lesson 2 done, lesson 3 (`format` + Pydantic, `exercises/samples/invoice_001.txt`, extract.py) published. Lesson 3 numbers checked on his machine: no format 0/5 parse; required missing `order_number` -> "conf. 100"; `str | None` at temperature 0 -> null.
- He writes to me in Italian: answer in Italian in chat, keep lessons in English.
- He skips the "why" questions in reports; name them one by one in the report list and answer the skipped ones in the feedback.
- Planned order: 2 temperature/seed -> 3 `format` (JSON schema output, first invoice-like extraction) -> 4 a first tiny eval set -> 5 tools.
