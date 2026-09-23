import os
import json
from openai import OpenAI

from tool import calculate_percentage

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

tool_definition = {
    "type": "function",
    "name": "calculate_percentage",
    "description": "Calculate the percentage when a student score and total marks are provided.",
    "parameters": {
        "type": "object",
        "properties": {
            "value": {
                "type": "number",
                "description": "The marks obtained by the student."
            },
            "total": {
                "type": "number",
                "description": "The total marks."
            }
        },
        "required": ["value", "total"],
        "additionalProperties": False
    }
}

question = "A student scored 45 marks out of 50. What is the percentage?"

print("=" * 60)
print("QUESTION:")
print(question)

# First request: ask the LLM whether it needs the tool
response = client.responses.create(
    model="openai/gpt-oss-20b",
    input=question,
    tools=[tool_definition]
)

for item in response.output:

    if item.type == "function_call":

        print("\nTOOL CALL:")
        print("Tool name:", item.name)
        print("Arguments:", item.arguments)

        arguments = json.loads(item.arguments)

        result = calculate_percentage(
            arguments["value"],
            arguments["total"]
        )

        print("\nTOOL RESULT:")
        print(result)

        # Send the tool result back to the model
        tool_result = {
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": result
        }

        response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=[
                {
                    "role": "user",
                    "content": question
                },
                {
                    "type": "function_call",
                    "call_id": item.call_id,
                    "name": item.name,
                    "arguments": item.arguments
                },
                tool_result
            ],
            tools=[tool_definition]
        )

print("\nFINAL ANSWER:")
print(response.output_text)