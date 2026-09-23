def chatbot(user_message):
    print("\n--- PLAIN CHATBOT ---")
    print("User:", user_message)

    response = """
I can provide a general answer about managing assignments.
However, I cannot directly access your private student_data.json file.
You would need to provide the assignment information to me.
"""

    print("Chatbot:", response)


user_input = input("Enter your question: ")

chatbot(user_input)