
import random
from datetime import datetime
from pathlib import Path


def check_motor():
    """Simulate changing motor sensor readings."""

    motor_data = {
        "temperature": round(random.uniform(40, 65), 2),
        "current": round(random.uniform(2.5, 4.5), 2),
        "vibration": round(random.uniform(0.10, 0.40), 3),
        "speed": random.randint(1320, 1480)
    }

    print("\n--- MOTOR SENSOR DATA ---")

    for sensor, value in motor_data.items():
        print(f"{sensor.capitalize()}: {value}")

    return motor_data


def analyze_motor(motor_data):
    """Classify motor health using demonstration rules."""

    temperature = motor_data["temperature"]
    current = motor_data["current"]
    vibration = motor_data["vibration"]
    speed = motor_data["speed"]

    faults = []
    warnings = []

    if temperature >= 60:
        faults.append("High temperature")
    elif temperature >= 50:
        warnings.append("Elevated temperature")

    if current >= 4.0:
        faults.append("High electrical current")
    elif current >= 3.2:
        warnings.append("Elevated electrical current")

    if vibration >= 0.35:
        faults.append("High vibration")
    elif vibration >= 0.25:
        warnings.append("Elevated vibration")

    if speed < 1350:
        faults.append("Low motor speed")
    elif speed < 1400:
        warnings.append("Reduced motor speed")

    if faults:
        condition = "Fault"
    elif warnings:
        condition = "Warning"
    else:
        condition = "Normal"

    print("\n--- RULE-BASED MOTOR ANALYSIS ---")
    print(f"Motor condition: {condition}")

    for item in faults:
        print(f"Fault indicator: {item}")

    for item in warnings:
        print(f"Warning indicator: {item}")

    if not faults and not warnings:
        print("No abnormal readings detected by the demonstration rules.")

    return condition


def generate_report(motor_data, condition, recommendation, confidence=None):
    """Save a motor maintenance report to a text file."""

    filename = Path(__file__).parent / "motor_report.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("INDUSTRIAL MOTOR MAINTENANCE REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        file.write("MOTOR SENSOR READINGS\n")
        file.write("-" * 25 + "\n")
        file.write(f"Temperature: {motor_data['temperature']} °C\n")
        file.write(f"Current: {motor_data['current']} A\n")
        file.write(f"Vibration: {motor_data['vibration']}\n")
        file.write(f"Speed: {motor_data['speed']} RPM\n\n")

        file.write(f"Predicted motor condition: {condition}\n")

        if confidence:
            file.write("\nAI PREDICTION CONFIDENCE\n")
            for label, probability in confidence.items():
                file.write(f"{label}: {probability}%\n")

        file.write(f"\nMaintenance recommendation: {recommendation}\n")
        file.write(
            "\nNOTE: Sensor readings are simulated. "
            "Recommendations and thresholds require validation "
            "before industrial use.\n"
        )

    print(f"Report saved as {filename.name}")
