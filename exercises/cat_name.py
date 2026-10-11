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
        counts[response.message.content] += 1
        if response.message.content is not None:
            clean_str: str = (response.message.content).strip()
    return counts


prompt = "Invent a name for a cat. Answer with the name only."
counts: collections.Counter = count_answers(prompt)
for answer, times in counts.most_common():
    print(times, answer)
print(len(counts), "different answers")
