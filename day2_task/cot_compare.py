from config import client, MODEL, banner


QUESTIONS = [

    """
    Three courses cost Rs. 12,000, Rs. 18,000 and Rs. 15,000.
    A student receives a 15% scholarship on the total amount
    and pays the remaining amount in 4 equal instalments.

    How much is each instalment?
    """,

    """
    A lab has 18 computers.
    In the morning, each computer is shared by 2 students.
    In the afternoon, each computer is shared by 3 students.

    How many student sittings happen in one day?
    """,

    """
    Ravi is taller than Kumar.
    Kumar is taller than Arun.
    Priya is shorter than Arun.

    Who is the tallest and who is the shortest?
    """
]


DIRECT_PROMPT = """
Give only the final answer.
Do not explain.
"""


COT_PROMPT = """
Solve the problem step by step.

Number each step and show the calculation or reasoning
in that step.

After the steps, write:

Final Answer: <answer>
"""


def ask(system_prompt, question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    banner("DIRECT PROMPTING vs CHAIN-OF-THOUGHT")

    for number, question in enumerate(QUESTIONS, start=1):

        print("\n" + "=" * 70)

        print(f"QUESTION {number}")
        print(question)

        print("\n--- WITHOUT CoT ---")

        direct_answer = ask(
            DIRECT_PROMPT,
            question
        )

        print(direct_answer)

        print("\n--- WITH CoT ---")

        cot_answer = ask(
            COT_PROMPT,
            question
        )

        print(cot_answer)