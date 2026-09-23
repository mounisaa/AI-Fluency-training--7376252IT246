from agent import agent


QUESTION = """
Which is cheaper:

Option 1:
CS101 and AI202 with a 10% scholarship

OR

Option 2:
CS101, AI202 and DS303 with a 25% scholarship?

The course fees must be obtained using the course-fee tool.

Calculate the final prices and tell me the difference.
"""


if __name__ == "__main__":

    print("=" * 70)
    print("REACT AGENT")
    print("=" * 70)

    print("\nQUESTION:")
    print(QUESTION)

    print("\n--- AGENT TRACE ---")

    answer = agent(
        QUESTION,
        max_steps=8
    )

    print("\n--- FINAL ANSWER ---")
    print(answer)