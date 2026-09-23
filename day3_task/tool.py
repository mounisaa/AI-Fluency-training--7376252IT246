def calculate_percentage(value, total):
    if total == 0:
        return "ERROR: Total cannot be zero."

    percentage = (value / total) * 100

    return f"Percentage = {percentage:.2f}%"


