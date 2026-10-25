# Valid vs correct understood; **kwargs forwarding and the role of the seed are not

On 2026-10-18 the user reported lesson 3 as done with `exercises/extract_data.py`. He explained in his own words that a supplier name that is wrong but well-formed passes Pydantic ("not logically right but semantically correct, so Pydantic did not intervene"): the valid-vs-correct distinction is in place. Next lessons can assume `format` + Pydantic and move to measuring correctness.

## Evidence

- `extract(text, options=options)` and `_ollama_call(..., options=options)` wrap the dict at each step, so `temperature` never reached Ollama. Verified: direct temperature=0 gives 1 distinct output of 5, his nested call gives 4 of 5. His "temperature 0" table row (5 of 10) is really the default temperature. Asked "what dict reaches Ollama?", he answered "the dict of extract": he did not see the wrapping.
- At real temperature 0, `invoice_001` gives the correct supplier (Ferramenta Rossi). His 6/10 "Officine Bianchi" (the customer) came from temperature 0.8.
- He proposed fixing `order_number` by finding a seed that gives the right value and keeping it. Misconception: the seed is a fix for one text, not a property of the system (and does nothing at temperature 0). Overfitting on one example.
- He did not say where "conf. 100" comes from ("Viti inox M6x30 (conf. 100)", conf. = confezione) and did not report the step 1 prediction.

## Implications

- Lesson 4 warm-up fixes the `**options` forwarding; quiz question on it. Recheck in lesson 5 when tools need argument dicts.
- Lesson 4 is the first eval (4 invoices, human ground truth, field score). Measured on his machine with my truth: lesson 3 extractor 13/24, + `Field(description=...)` 13/24 (format does not show the schema to the model), + schema in the prompt 20/24. Remaining failures: dates `25-09-2026` and `30 settembre 2026` not converted, supplier of invoice_002 (listed under "Emessa da:" at the bottom).
