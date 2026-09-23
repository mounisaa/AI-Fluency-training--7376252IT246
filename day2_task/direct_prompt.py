from config import client, MODEL, banner


QUESTION = """
Three courses cost Rs. 12,000, Rs. 18,000 and Rs. 15,000.
A student receives a 15% scholarship on the total amount
and pays the remaining amount in 4 equal instalments.

How much is each instalment?
"""


def ask_direct(question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Give only the final answer. Do not explain."
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

    banner("DIRECT PROMPTING")

    print("QUESTION:")
    print(QUESTION)

    print("\nANSWER:")
    print(ask_direct(QUESTION))