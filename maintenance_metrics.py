
from datetime import datetime
from pathlib import Path
import json
from excel_logger import save_maintenance_event

EVENT_FILE = Path(__file__).parent / "maintenance_events.json"


def load_events():
    if EVENT_FILE.exists():
        with open(EVENT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


def save_events(events):
    with open(EVENT_FILE, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)


def record_failure():
    events = load_events()

    failure_time = datetime.now().isoformat()

    events.append({
        "event": "failure",
        "time": failure_time
    })

    save_events(events)

    save_maintenance_event(
        "Breakdown",
        "Confirmed machine breakdown"
    )

    print("Machine breakdown recorded.")



def record_repair():
    events = load_events()

    repaired_failures = {
        event["failure_time"]
        for event in events
        if event["event"] == "repair"
    }

    pending = [
        event for event in events
        if event["event"] == "failure"
        and event["time"] not in repaired_failures
    ]

    if not pending:
        print("No outstanding breakdown found.")
        return

    failure = pending[-1]
    repair_time = datetime.now()
    failure_time = datetime.fromisoformat(failure["time"])

    repair_hours = (
        repair_time - failure_time
    ).total_seconds() / 3600

    events.append({
        "event": "repair",
        "failure_time": failure["time"],
        "time": repair_time.isoformat(),
        "repair_hours": round(repair_hours, 4)
    })

    save_events(events)

    save_maintenance_event(
        "Repair",
        "Repair completed for recorded breakdown",
        round(repair_hours, 4)
    )

    print("Repair recorded.")
    print(f"Repair duration: {repair_hours:.4f} hours")
    print(f"Repair duration: {repair_hours * 60:.2f} minutes")


    if not pending:
        print("No outstanding breakdown found.")
        return

    failure = pending[-1]
    repair_time = datetime.now()
    failure_time = datetime.fromisoformat(failure["time"])

    repair_hours = (
        repair_time - failure_time
    ).total_seconds() / 3600

    events.append({
        "event": "repair",
        "failure_time": failure["time"],
        "time": repair_time.isoformat(),
        "repair_hours": round(repair_hours, 4)
    })

    save_events(events)

    print("Repair recorded.")
    print(f"Repair duration: {repair_hours:.4f} hours")


def show_mttr():
    events = load_events()

    repairs = [
        event["repair_hours"]
        for event in events
        if event["event"] == "repair"
    ]

    print("\n--- MAINTENANCE METRICS ---")

    if not repairs:
        print("MTTR: Not available yet. Record and repair a breakdown first.")
        return

    mttr = sum(repairs) / len(repairs)

    print(f"Confirmed repairs: {len(repairs)}")
    print(f"MTTR: {mttr:.4f} hours")
    print(f"MTTR: {mttr * 60:.2f} minutes")

def show_mtbf():
    events = load_events()

    failures = [
        event for event in events
        if event["event"] == "failure"
    ]

    if len(failures) < 2:
        print("\n--- MTBF ---")
        print("MTBF: Not available yet.")
        print("Record at least two breakdowns to calculate MTBF.")
        return

    intervals = []

    for i in range(1, len(failures)):
        previous_failure = datetime.fromisoformat(
            failures[i - 1]["time"]
        )
        current_failure = datetime.fromisoformat(
            failures[i]["time"]
        )

        interval_hours = (
            current_failure - previous_failure
        ).total_seconds() / 3600

        intervals.append(interval_hours)

    mtbf = sum(intervals) / len(intervals)

    print("\n--- MTBF ---")
    print(f"Confirmed failures: {len(failures)}")
    print(f"MTBF: {mtbf:.4f} hours")
    print(f"MTBF: {mtbf * 60:.2f} minutes")


def show_availability():
    from machine_runtime import load_state

    state = load_state()

    running_seconds = state["total_running_seconds"]

    if state["status"] == "RUNNING":
        started = datetime.fromisoformat(state["last_started"])
        running_seconds += (
            datetime.now() - started
        ).total_seconds()

    scheduled_hours = 8
    running_hours = running_seconds / 3600

    availability = min(
        running_hours / scheduled_hours * 100,
        100
    )

    print("\n--- MACHINE AVAILABILITY ---")
    print(f"Scheduled shift: {scheduled_hours:.2f} hours")
    print(f"Accumulated running time: {running_hours:.4f} hours")
    print(f"Availability: {availability:.2f}%")
    print("\nNote: Simulation uses a fixed 8-hour shift.")

