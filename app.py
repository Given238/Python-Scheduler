import json


def save_data(data):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "tasks": [],
            "events": [],
            "reminders": []
        }


def show_menu():
    print("1. Add Task")
    print("2. Add Event")
    print("3. Add Reminder")
    print("4. View All Items")
    print("5. Exit")


def main():
    # Load existing data or initialize new data (tasks, events, reminders) from the JSON file (step 1)
    data = load_data()
    while True:
        show_menu()
        choice = input("Enter your choice:").strip()

        if choice == '1':
            task = input("Enter the task:")
            data["tasks"].append(task)
            print(f"Task '{task}' added successfully!")
            save_data(data)
        elif choice == '2':
            event = input("Enter the event:")
            data["events"].append(event)
            print(f"Event '{event}' added successfully!")
            save_data(data)
        elif choice == '3':
            reminder = input("Enter the reminder:")
            data["reminders"].append(reminder)
            print(f"Reminder '{reminder}' added successfully!")
            save_data(data)
        elif choice == '4':
            for category in ["tasks", "events", "reminders"]:
                print(f"\n{category.capitalize()}:")
                if not data[category]:
                    print("No items found.")
                else:
                    for item in data[category]:
                        print(f"- {item}")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        save_data(data)

        # Note for tomorrow: add details to tasks, events, and reminders.


if __name__ == "__main__":
    main()
