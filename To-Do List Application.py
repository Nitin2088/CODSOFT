# To-Do List Application

# Initialize an empty dictionary to store tasks
tasks = {}

# Function to add a task
def add_task():
    task_name = input("Enter the task: ")
    tasks[task_name] = False
    print(f"Task '{task_name}' added.")

# Function to view tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for task, completed in tasks.items():
            status = "Done" if completed else "Not Done"
            print(f"{task} - {status}")
    else:
        print("No tasks in the list.")

# Function to mark a task as complete
def complete_task():
    task_name = input("Enter the task to mark as complete: ")
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Task '{task_name}' marked as complete.")
    else:
        print(f"Task '{task_name}' not found in the list.")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
