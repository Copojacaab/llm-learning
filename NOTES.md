# Notes

- Lessons and references in English. User speaks English but doesn't think in it as natively as in Italian: simple sentences, clear technical terms.
- 30 minutes per lesson, one per day.
- Learn by doing on real cases: track A on his own work, track B (code) in longer weekend blocks.
- Recommend communities for the "wisdom" part (optional).
- Lesson 1: install Ollama (and raise the WSL RAM limit in .wslconfig, currently 7.6 GB visible), call a local model from Python. No ollama/uv installed yet; Python 3.14.
- Local models first; hand-written agent loop; then compare against Claude on the same tasks. Teach output constraints, evals, fallback since 7-8B models are fragile at tool use.
- Use sample/anonymized documents for invoices until the company confirms data rules.
- Secretary v1 = morning briefing only; add one function at a time.
