import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

questions = [
    "What is an LLM in simple words?",
    "What is the capital of France?",
    "A student scored 45 marks out of 50. What is the percentage?"
]

for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:")
    print(question)

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=question
    )

    print("\nPLAIN LLM ANSWER:")
    print(response.output_text)