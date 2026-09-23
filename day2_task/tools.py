COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code):
    """
    Return the fee of a course.
    """

    course_code = course_code.upper()

    if course_code in COURSE_FEES:
        return COURSE_FEES[course_code]

    return f"Course {course_code} not found"


def calculator(expression):
    """
    Calculate a mathematical expression.
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return result

    except Exception as e:
        return f"Calculation error: {e}"


# Tool definitions for the AI model

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Return the fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "The course code, such as CS101, AI202, or DS303."
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
                        "description": "A mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]