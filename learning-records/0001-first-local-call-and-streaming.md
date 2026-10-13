# First local call works; streaming understood as delivery, not a different generation

On 2026-10-10 the user completed lesson 1: Ollama 0.40.1 + `llama3.2:3b` run on his GPU and his own script (`exercises/hello_llm.py`) calls `chat()`, also with `stream=True`. He described streaming in his own words as "each token is sent at once instead of accumulated", which is correct. Next lessons can assume the request/response shape of `chat()` and build on `options`, `format`, `tools`.

## Evidence

- Working script with streaming loop in `exercises/hello_llm.py`.
- He noticed the second run was faster but asked why: `load_duration` / `keep_alive` was not yet linked to the observation (explained on 2026-10-10, re-tested in the lesson 2 quiz).
- Quiz "all correct" is weak evidence: in lesson 1 the right option was always the first one (fixed, `quiz.js` now shuffles).

## Implications

- With `stream=True` he commented out the tokens/s lines: he did not know the statistics are in the last chunk. Lesson 2 warm-up covers it.
- He judged repeated answers as "more or less the same". At default temperature they are 6 different strings out of 6. This gap (looks the same vs is the same) is the entry point to evals.
