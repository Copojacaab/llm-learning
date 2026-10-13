# Temperature and seed measured with his own tool; the two "why" questions were skipped

On 2026-10-13 the user reported lesson 2 as done. He wrote `exercises/repeat.py` himself (with `argparse` flags for temperature and seed, beyond the spec) and filled the table: default 4 different names out of 10, temperature 0 gives 1, temperature 1.5 gives 7, each seed gives 1. His prediction for the default run was 7, so he expected more randomness than there is at 0.8. Next lessons can assume `options`, temperature 0 for extraction, and counting with `Counter`.

## Evidence

- Table in the docstring at the end of `exercises/repeat.py`. Re-run on his machine the same day: 3 / 1 / 8 / 1 / 1, same names (`Zhilakai` at temperature 0, `Lysandra` at seed 42).
- The two questions of step 3 were not answered (is the temperature 0 name the most common default name; how many of 10 venv sentences are equal). Measured for him: yes (`Zhilakai` 7 of 10 at default) and 10 different sentences out of 10.
- Seed 7 gave the same name as temperature 0. He did not comment on it. Seeds 7 and 8 both give `Zhilakai`, seeds 1-6 give six other names: a random pick often lands on the likeliest token.

## Implications

- `count_answers` counts the raw string and computes `.strip()` afterwards into an unused variable. He read the spec but did not check that the cleaned value is the one used. Lesson 3 warm-up asks him to fix it.
- He reports numbers but skips the "why" questions. Keep them few, and ask for them by name in the report list. The seed 7 coincidence is in the lesson 3 quiz.
- Still open from lesson 1: `hello.py` prints `"/n"` instead of `"\n"`.
