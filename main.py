from datetime import datetime

events = [
    {
        "date": "2026-07-15",
        "title": "Team Meeting"
    },
    {
        "date": "2026-07-18",
        "title": "Doctor Appointment"
    },
    {
        "date": "2026-07-22",
        "title": "Birthday Party"
    },
    {
        "date": "2026-07-28",
        "title": "Weekend Trip"
    }
]


def sort_events(data):
    return sorted(data, key=lambda event: event["date"])


def print_events(data):
    print("=" * 32)
    print("      UPCOMING EVENTS")
    print("=" * 32)

    for event in data:
        print(f"{event['date']} | {event['title']}")

    print("-" * 32)
    print(f"Total events: {len(data)}")
    print(f"Next event: {data[0]['title']}")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 32)


def main():
    upcoming = sort_events(events)
    print_events(upcoming)


if __name__ == "__main__":
    main()
