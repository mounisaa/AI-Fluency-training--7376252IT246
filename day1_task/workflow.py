import json
from datetime import datetime


def load_data():
    with open("student_data.json", "r") as file:
        return json.load(file)


def workflow():
    print("\n--- RULE-BASED WORKFLOW ---")

    data = load_data()

    pending_tasks = []

    for assignment in data["assignments"]:

        if assignment["status"] == "Pending":
            pending_tasks.append(assignment)

    pending_tasks.sort(
        key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d")
    )

    print("\nPending assignments:")

    for task in pending_tasks:
        print(
            f"- {task['subject']}: "
            f"{task['task']} | "
            f"Deadline: {task['deadline']} | "
            f"Priority: {task['priority']}"
        )


workflow()