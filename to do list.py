import json
import os

# File to store tasks
FILE_NAME = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    else:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show menu options
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as completed")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            status = "✔️ Done" if task["completed"] else "❌ Not Done"
            print(f"{i}. {task['title']} - {status}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Edit a task
def edit_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        new_title = input("Enter new title: ")
        tasks[index]["title"] = new_title
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()

