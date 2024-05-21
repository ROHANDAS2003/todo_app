# todo_app.py

# Function to display the current tasks
def display_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Current Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("No tasks yet!")
    except FileNotFoundError:
        print("No tasks yet!")

# Function to add a new task
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Function to mark a task as complete
def mark_task_complete(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for idx, task in enumerate(tasks, start=1):
                if idx == task_number:
                    file.write(task.replace("[ ]", "[x]", 1))
                else:
                    file.write(task)
        print("Task marked as complete!")
    except FileNotFoundError:
        print("No tasks yet!")

# Function to delete a task
def delete_task(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for idx, task in enumerate(tasks, start=1):
                if idx != task_number:
                    file.write(task)
        print("Task deleted successfully!")
    except FileNotFoundError:
        print("No tasks yet!")

# Main function
def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task("[ ] " + task)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            mark_task_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
