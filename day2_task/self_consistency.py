from collections import Counter

from config import client, MODEL, banner
from cot_compare import COT_PROMPT, QUESTIONS


RUNS = 5
TEMPERATURE = 0.8


def final_answer(text):

    for line in reversed(text.splitlines()):

        if "final answer" in line.lower():

            return line.split(":", 1)[-1].strip()

    lines = text.splitlines()

    if lines:
        return lines[-1].strip()

    return "(empty)"


def run_many(question):

    answers = []

    for attempt in range(1, RUNS + 1):

        response = client.chat.completions.create(

            model=MODEL,

            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],

            temperature=TEMPERATURE
        )

        answer = final_answer(
            response.choices[0].message.content
        )

        print(f"Run {attempt}: {answer}")

        answers.append(answer)

    return answers


if __name__ == "__main__":

    banner("SELF-CONSISTENCY")

    question = QUESTIONS[0]

    print("QUESTION:")
    print(question)

    print("\n--- FIVE RUNS ---")

    answers = run_many(question)

    winner, count = Counter(answers).most_common(1)[0]

    print("\nMajority Answer:")
    print(winner)

    print(
        f"\nMajority count: {count} out of {len(answers)}"
    )