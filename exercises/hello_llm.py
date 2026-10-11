from ollama import chat

response = chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "In one sentence: what is a Python venv?"}],
    stream=True,
)

for chunk in response:
    print(chunk.message.content, end="", flush=True)
print("/n")
if chunk is not None and chunk.done:
    seconds = chunk.eval_duration / 1e9
    print(f"{chunk.eval_count} tokens, {chunk.eval_count / seconds} tokens/s")

# seconds = response.eval_duration / 1e9
# print(f"{response.eval_count} tokens; {response.eval_count / seconds} token/s")
# print(f"{seconds} sec")
