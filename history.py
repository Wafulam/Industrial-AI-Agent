
import csv
from pathlib import Path
from datetime import datetime


HISTORY_FILE = Path(__file__).parent / "motor_history.csv"


def save_reading(motor_data, condition):
    """Save one motor reading to the history CSV file."""

    file_exists = HISTORY_FILE.exists()

    with open(
        HISTORY_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "temperature",
                "current",
                "vibration",
                "speed",
                "condition"
            ])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            motor_data["temperature"],
            motor_data["current"],
            motor_data["vibration"],
            motor_data["speed"],
            condition
        ])

    print(f"Reading saved to {HISTORY_FILE.name}")
    
def analyze_history():
    """Analyze trends in saved motor sensor readings."""

    import csv

    if not HISTORY_FILE.exists():
        print("No motor history found. Run 'check motor' first.")
        return

    with open(HISTORY_FILE, "r", newline="", encoding="utf-8") as file:
        readings = list(csv.DictReader(file))

    if len(readings) < 2:
        print("At least two readings are needed to analyze trends.")
        return

    sensors = ["temperature", "current", "vibration", "speed"]

    print("\n--- MOTOR HISTORICAL TREND ANALYSIS ---")
    print(f"Readings analyzed: {len(readings)}")

    for sensor in sensors:
        values = [float(row[sensor]) for row in readings]
        first = values[0]
        latest = values[-1]
        change = latest - first

        if change > 0:
            direction = "increased"
        elif change < 0:
            direction = "decreased"
        else:
            direction = "unchanged"

        print(
            f"{sensor.capitalize()}: {first:.2f} -> "
            f"{latest:.2f} ({direction}, change: {change:+.2f})"
        )

    print(
        "\nNote: This compares the first and latest readings. "
        "It does not prove a fault or predict remaining motor life."
    )

