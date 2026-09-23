from config import client, MODEL
from tools import get_course_fee, calculator


# Tool definitions for the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202 or DS303"
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to calculate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


def execute_tool(tool_name, arguments):

    if tool_name == "get_course_fee":
        return get_course_fee(
            arguments["course_code"]
        )

    elif tool_name == "calculator":
        return calculator(
            arguments["expression"]
        )

    return "Unknown tool"


def agent(question, max_steps=8):

    messages = [
        {
            "role": "system",
            "content": """
You are a ReAct agent.

Use the available tools when necessary.

Follow this process:

Thought → Action → Observation

Available tools:

- get_course_fee(course_code)
- calculator(expression)

Do not invent course fees.

First obtain the required course fees using get_course_fee.

Then use calculator for the calculations.

When you have enough information, provide the final answer.
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        # If the model wants to call a tool
        if message.tool_calls:

            messages.append(message)

            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name

                import json

                arguments = json.loads(
                    tool_call.function.arguments
                )

                print(f"\nStep {step}")
                print(f"Action: {tool_name}")
                print(f"Arguments: {arguments}")

                result = execute_tool(
                    tool_name,
                    arguments
                )

                print(f"Observation: {result}")

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    }
                )

            continue

        # No more tools required
        final_answer = message.content

        print(f"\nStep {step}")
        print("Final Answer:")
        print(final_answer)

        return final_answer

    return "Maximum steps reached."