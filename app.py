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
            task_date = input("Enter date and time for the task:")
            task_duration = input("Enter duration for the task:")
            task_description = input("Enter a description for the task:")
            data["tasks"].append({
                "name": task,
                "date": task_date,
                "duration": task_duration,
                "description": task_description
            })
            print(f"Task '{task}' added successfully!")
            save_data(data)
        elif choice == '2':
            event = input("Enter the event:")
            event_date = input("Enter date and time for event:")
            event_location = input("Enter location for event:")
            event_duration = input("Enter duration for event:")
            event_description = input("Enter a description for the event:")
            data["events"].append({
                "name": event,
                "date": event_date,
                "location": event_location,
                "duration": event_duration,
                "description": event_description
            })
            print(f"Event '{event}' added successfully!")
            save_data(data)
        elif choice == '3':
            reminder = input("Enter the reminder:")
            reminder_deadline = input("Enter deadline for the reminder:")
            data["reminders"].append({
                "name": reminder,
                "deadline": reminder_deadline,
            })
            print(f"Reminder '{reminder}' added successfully!")
            save_data(data)
        elif choice == '4':
            for category in ["tasks", "events", "reminders"]:
                print(f"\n{category.capitalize()}:")
                if not data[category]:
                    print("No items found.")
                else:
                    for item in data[category]:
                        if not isinstance(item, dict):
                            print(f"- Invalid {category[:-1]} entry: {item}")
                            continue

                        if category == "tasks":
                            print(
                                f"- Task: {item.get('name', 'N/A')}\n  Date/Time: {item.get('date', 'N/A')}\n  Duration: {item.get('duration', 'N/A')}\n  Description: {item.get('description', 'N/A')}")
                        elif category == "events":
                            print(
                                f"- Event: {item.get('name', 'N/A')}\n  Date/Time: {item.get('date', 'N/A')}\n  Location: {item.get('location', 'N/A')}\n  Duration: {item.get('duration', 'N/A')}\n  Description: {item.get('description', 'N/A')}")
                        elif category == "reminders":
                            print(
                                f"- Reminder: {item.get('name', 'N/A')}\n  Deadline: {item.get('deadline', 'N/A')}")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        save_data(data)

        # Note for tomorrow: add details to tasks, events, and reminders. (done 2026-04-02)
        # Next, add error handling for invalid inputs and ensure that the application can handle edge cases gracefully.


if __name__ == "__main__":
    main()
