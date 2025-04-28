#Changes to make to go from: To do list -> Checklist
# Dont use input() -> apps frontend will give the data
# Turn your functions into methods that accept parameters (like add_task(task)) instead of asking for input
# Store the tasks permanently (save to JSON file) - because when you close the app, your list would otherwise disappear
# Return data - not print() everywhere - so the frontend (Kivy GUI) can display it nicely

#DataStorage


tasks = []

def AddTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' was added to the list.")

def DeleteTask():
    ListTasks()
    try:
        TaskToDelete = int(input("Enter the # of the task to delete: "))
        if TaskToDelete >= 0 and TaskToDelete < len(tasks):
            tasks.pop(TaskToDelete)
            print(f"Task #{TaskToDelete} was deleted.")
        else:
            print(f"Task #{TaskToDelete} was not found.")

    except:
        print("Something went wrong.")

def ListTasks():
    if not tasks:
        print("No tasks were found.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}. {task}")

if __name__ == "__main__":
    print("Welcome to the Checklist App :)")

while True:
    print("\n")
    print("Select one of the options:")
    print("----------------------------------")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. List all tasks")
    print("4. Quit")
    print("\n")

    choice = input("Enter your choice: ")
    if choice == "1":
        AddTask()
    elif choice == "2":
        DeleteTask()
    elif choice == "3":
        ListTasks()
    elif choice == "4":
        break
    else:
        print("Invalid input. Please try again.")
