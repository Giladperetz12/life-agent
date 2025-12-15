import json
from pathlib import Path
from datetime import datetime


def load_events():
    path = Path("data/calendar.json")
    with path.open("r", encoding="utf-8") as f:
        events = json.load(f)
    if not events:
        print("No calendar events found.")
        events = []
    return events



def parse_time(time_str):
    return datetime.fromisoformat(time_str)


def find_overlaps(events):
    overlaps = []

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            event_1 = events[i]
            event_2 = events[j]

            start_1 = parse_time(event_1["start_time"])
            end_1 = parse_time(event_1["end_time"])
            start_2 = parse_time(event_2["start_time"])
            end_2 = parse_time(event_2["end_time"])

            if start_1 < end_2 and start_2 < end_1:
                overlaps.append((event_1, event_2))
    return overlaps
