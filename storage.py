import json
from pathlib import Path


def save_data(data):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    path = Path("tasks.json")
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "tasks": [],
            "events": [],
            "reminders": [],
            "week_schedule": create_empty_week_schedule(),
        }
    except json.JSONDecodeError:
        # Incomplete/corrupt save (e.g. crash mid-write). Keep the bad file for inspection.
        bad = path.with_name("tasks.json.invalid")
        try:
            path.rename(bad)
        except OSError:
            pass
        print(
            "Warning: tasks.json was not valid JSON. "
            f"It was renamed to {bad.name} if possible. Starting with empty data."
        )
        return {
            "tasks": [],
            "events": [],
            "reminders": [],
            "week_schedule": create_empty_week_schedule(),
        }
