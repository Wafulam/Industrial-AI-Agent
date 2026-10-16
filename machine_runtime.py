
from datetime import datetime
from pathlib import Path
import json

STATE_FILE = Path(__file__).parent / "machine_runtime.json"


def load_state():
    """Load the saved machine runtime state."""

    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {
        "status": "STOPPED",
        "last_started": None,
        "total_running_seconds": 0
    }


def save_state(state):
    """Save machine runtime state to disk."""

    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(state, file, indent=4)


def start_machine():
    """Simulate starting the machine."""

    state = load_state()

    if state["status"] == "RUNNING":
        print("Machine is already running.")
        return

    state["status"] = "RUNNING"
    state["last_started"] = datetime.now().isoformat()

    save_state(state)

    print("Machine started.")
    print(f"Start time: {state['last_started']}")


def stop_machine():
    """Stop the machine and accumulate its running time."""

    state = load_state()

    if state["status"] != "RUNNING":
        print("Machine is already stopped.")
        return

    now = datetime.now()
    started = datetime.fromisoformat(state["last_started"])

    running_seconds = (now - started).total_seconds()

    state["total_running_seconds"] += running_seconds
    state["status"] = "STOPPED"
    state["last_started"] = None

    save_state(state)

    print("Machine stopped.")
    print(f"Running time this session: {running_seconds / 3600:.4f} hours")


def show_runtime():
    """Display accumulated machine running hours."""

    state = load_state()
    total_seconds = state["total_running_seconds"]

    if state["status"] == "RUNNING":
        started = datetime.fromisoformat(state["last_started"])
        total_seconds += (datetime.now() - started).total_seconds()

    print("\n--- MACHINE RUNTIME ---")
    print(f"Status: {state['status']}")
    print(f"Total running hours: {total_seconds / 3600:.4f}")
