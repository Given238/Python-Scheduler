from storage import save_data, load_data
from datetime import datetime, timedelta


# L7 - L76: functions for validating user input/error handling
# prompt_non_empty: prompt the user to enter a non-empty value
# _normalize_am_pm: normalize the AM/PM to the correct format
# prompt_date: prompt the user to enter a date and time
# prompt_duration: prompt the user to enter a duration
# prompt_deadline: prompt the user to enter a deadline

def prompt_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def _normalize_am_pm(text):
    """strptime %p expects AM/PM; users often type A.M / P.M."""
    return (
        text.replace("A.M", "AM")
        .replace("P.M", "PM")
        .replace("a.m", "am")
        .replace("p.m", "pm")
    )


def _to_json_value(value):
    """JSON cannot store datetime/timedelta; convert to strings before saving."""
    if isinstance(value, datetime):
        return value.isoformat(timespec="seconds")
    if isinstance(value, timedelta):
        return str(value)
    return value


def prompt_date(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Date and time cannot be empty. Please try again.")
            continue

        value = _normalize_am_pm(value)
        try:
            # %I = 12-hour clock (01–12). Do not use %H here with AM/PM.
            parsed_date = datetime.strptime(value, "%d %B %Y, %I:%M %p")
            return parsed_date
        except ValueError:
            print(
                "Invalid format. Use 12-hour time with AM or PM, e.g. "
                "'7 March 2026, 04:00 PM' or '17 August 2026, 03:00 A.M'. "
                "Do not mix 24-hour (e.g. 16:00) with P.M. Please try again.")
            continue


def prompt_duration(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Duration cannot be empty. Please try again.")
            continue
        try:
            parsed_duration = timedelta(minutes=int(value))
            return parsed_duration
        except ValueError:
            print(
                f"Invalid duration format: '{value}'. Use the format: '120' Please try again.")
            continue


def prompt_deadline(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Deadline cannot be empty. Please try again.")
            continue
        value = _normalize_am_pm(value)
        try:
            parsed_deadline = datetime.strptime(value, "%d %B %Y, %I:%M %p")
            return parsed_deadline
        except ValueError:
            print(
                "Invalid format. Use 12-hour time with AM or PM, e.g. "
                "'7 March 2026, 04:00 PM' or '17 August 2026, 03:00 A.M'. "
                "Do not mix 24-hour (e.g. 16:00) with P.M. Please try again.")
            continue


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
            task = prompt_non_empty("Enter the task:")
            task_date = prompt_date("Enter date and time for the task:")
            task_duration = prompt_duration("Enter duration for the task:")
            task_description = prompt_non_empty(
                "Enter a description for the task:")
            data["tasks"].append({
                "name": task,
                "date": _to_json_value(task_date),
                "duration": _to_json_value(task_duration),
                "description": task_description
            })
            print(f"Task '{task}' added successfully!")
            save_data(data)
        elif choice == '2':
            event = prompt_non_empty("Enter the event:")
            event_date = prompt_date("Enter date and time for event:")
            event_location = prompt_non_empty("Enter location for event:")
            event_duration = prompt_duration("Enter duration for event:")
            event_description = prompt_non_empty(
                "Enter a description for the event:")
            data["events"].append({
                "name": event,
                "date": _to_json_value(event_date),
                "location": event_location,
                "duration": _to_json_value(event_duration),
                "description": event_description
            })
            print(f"Event '{event}' added successfully!")
            save_data(data)
        elif choice == '3':
            reminder = prompt_non_empty("Enter the reminder:")
            reminder_deadline = prompt_deadline(
                "Enter deadline for the reminder:")
            data["reminders"].append({
                "name": reminder,
                "deadline": _to_json_value(reminder_deadline),
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

        # Personal notes(Given):

        # Note for tomorrow: add details to tasks, events, and reminders. (done 2026-04-02)
        # Next, add error handling for invalid inputs and ensure that the application can handle edge cases gracefully.(done 2026-04-05)
        # Finally, make code more realable, handle storage better (e.g. handle incomplete/corrupt saves, do not crash if tasks.json is invalid, etc.)
        # Then, Move on to next step, expand functionality (e.g. editing/deleting tasks, events, reminders; adding categories/tags; etc.) -> CRUD operations for tasks/events/reminders, categories/tags, etc.
        # Then, your project is basically done! You can stop here or add more features as you like (e.g. notifications, recurring tasks/events/reminders, etc.). You can also improve the user interface (e.g. add colors, formatting, etc.) if you want to.


if __name__ == "__main__":
    main()
