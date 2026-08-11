import json
import os

FILE_NAME = "ToDo_tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Unable to load saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Could not save tasks.")


def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter task name: ").strip()

    if not task_name:
        print("Task name cannot be empty.")
        return

    task = {
        "title": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n---------- TO-DO LIST ----------")

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")

    print("--------------------------------")


def mark_task_done(tasks):
    """Mark a selected task as completed."""
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark as done: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[task_number - 1]

        if task["completed"]:
            print("This task is already completed.")
        else:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """Delete a selected task."""
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)

        print(f"Deleted task: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main menu of the To-Do List Manager."""
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST MANAGER ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using the To-Do List Manager!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
