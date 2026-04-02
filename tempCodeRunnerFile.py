def show_menu():
    print("1. Add Task")
    print("2. Add Event")
    print("3. Add Reminder")
    print("4. Exit")


def main():
    show_menu()
    while True:

        choice = input("Enter your choice:")

        if choice == '1':
            task = input("Enter the task:")
            print(f"Task '{task}' added successfully!")
        elif choice == '2':
            event = input("Enter the event:")
            print(f"Event '{event}' added successfully!")
        elif choice == '3':
            reminder = input("Enter the reminder:")
            print(f"Reminder '{reminder}' added successfully!")
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break


if __name__ == "__main__":
    main()
