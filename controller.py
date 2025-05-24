from groq import Groq
from models import Response

history = []

def call_groq(input):
    query = input.query
    client = Groq()

    if not history:
        history.append({"role": "system", "content": "you are a helpful assistant"})

    history.append({"role": "user", "content": query})

    completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=history
    )
    answer = completion.choices[0].message.content.strip()
    usages = completion.usage.completion_tokens

    print(f"Usages: {usages}")

    history.append({"role": "assistant", "content": answer})

    print(history)

    return Response(answer=answer).fetch_answer()