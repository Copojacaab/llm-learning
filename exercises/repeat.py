import argparse

import ollama
import collections


def count_answers(prompt: str, n=10, **options) -> collections.Counter:
    counts: collections.Counter = collections.Counter()

    for _ in range(n):
        response: ollama.ChatResponse = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options=options,
        )
        if response.message.content is not None:
            clean_str: str = (response.message.content).strip()
        counts[clean_str] += 1

    return counts


if __name__ == "__main__":
    # === parser
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Prende temperature e seed come argomenti"
    )
    parser.add_argument("--temperature", required=False, type=float)
    parser.add_argument("--seed", required=False, type=int)
    args = parser.parse_args()

    temperature = args.temperature
    seed = args.seed

    print(f"temperature: {temperature}, seed: {seed}")
    print()
    # ====

    prompt = "Invent a name for a cat. Answer with the name only."
    counts: collections.Counter = count_answers(
        prompt, temperature=temperature, seed=seed
    )
    for answer, times in counts.most_common():
        print(times, answer)
    print(len(counts), "different answers")

"""
================================== RESULTS ==================================
                call                          different answers out of ten
=============================================================================
(prompt)                                      4
(prompt, temperature=0)                       1 Zhilakai
(prompt, temperature=1.5)                     7 
(prompt, temperature=1.5, seed=42)            1 Lysandra
(prompt temperature=1.5, seed=7)              1 Zhilakai
"""
