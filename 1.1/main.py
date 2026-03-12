from utils import add_task, show_tasks, delete_task
from config import APP_NAME, VERSION

def main():
    print(f"=== {APP_NAME} ===")
    print(f"=== {VERSION} ===")

    tasks = []

    while True:
        print("\n1 - Add task")
        print("2 - Show tasks")
        print("3 - Delete task")
        print("4 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        elif choice == '3':
            task = input("Enter task: ")
            if task in tasks:
                delete_task(tasks, task)
            else:
                pass

        else:
            print("Invalid option")


main()