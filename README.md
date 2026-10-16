# Industrial Maintenance AI Agent

An AI-assisted predictive maintenance prototype that analyzes simulated industrial motor sensor readings, predicts motor health conditions, generates maintenance alerts, and records maintenance information for review.

## Project Overview

Unexpected motor failures can cause production downtime, maintenance costs, and equipment damage. This project explores how machine learning and maintenance data tracking can help identify potential motor problems earlier.

The prototype combines a trained machine-learning model with a Python command-line agent and Excel-based maintenance records.

## Features

- **Motor health prediction:** Classifies simulated motor readings as Normal, Warning, or Fault.
- **Sensor simulation:** Generates temperature, electrical current, vibration, and motor speed readings.
- **Maintenance recommendations:** Displays guidance based on the predicted motor condition.
- **Automatic alerts:** Logs predicted Warning and Fault conditions.
- **Excel logging:** Stores motor readings, predictions, confidence values, recommendations, breakdowns, and repairs.
- **Runtime tracking:** Simulates machine start and stop events and accumulates running hours.
- **Maintenance metrics:** Calculates MTTR and an initial elapsed-time MTBF.
- **Availability estimate:** Demonstrates a simplified availability calculation against an eight-hour shift.
- **Maintenance summary:** Generates an Excel worksheet summarizing key maintenance indicators.
- **Historical records:** Maintains CSV and JSON data for analysis.

## Technology Stack

- Python
- pandas
- scikit-learn
- joblib
- openpyxl
- Excel
- VS Code
- Git and GitHub

## Project Structure

```text
Industrial-AI-Agent/
├── agent.py
├── tools.py
├── motor_ai.py
├── history.py
├── excel_logger.py
├── machine_runtime.py
├── maintenance_metrics.py
├── maintenance_summary.py
├── motor_history.csv
├── maintenance_events.json
├── motor_maintenance.xlsx
└── README.md
```

The project also uses a trained model stored in the separate `motor-ai` project directory.

## Getting Started

1. Install Python 3.11 or a compatible version.
2. Open this project folder in VS Code.
3. Create and activate a virtual environment.
4. Install the required packages:

```bash
pip install pandas scikit-learn joblib openpyxl
```

5. Ensure the trained model file `motor_model.pkl` is available at the location expected by `motor_ai.py`.
6. Run the agent:

```bash
python agent.py
```

## Available Commands

| Command | Purpose |
|---|---|
| `check motor` | Generate readings and predict motor condition |
| `history` | Review historical readings |
| `alerts` | View logged AI alerts |
| `report` | Generate a maintenance report |
| `start machine` | Simulate machine startup |
| `stop machine` | Simulate machine shutdown |
| `runtime` | View accumulated running hours |
| `record failure` | Record a confirmed simulated breakdown |
| `record repair` | Record a repair |
| `mttr` | Calculate average recorded repair duration |
| `mtbf` | View elapsed time between recorded failures |
| `availability` | Calculate a simplified availability estimate |
| `summary` | Refresh the Excel maintenance summary |
| `exit` | Close the agent |

## Important Limitations

This is an educational prototype. Sensor readings and machine operation are simulated; the system is not connected to a physical motor or PLC.

The current availability calculation uses a fixed eight-hour shift. MTBF currently measures elapsed clock time between recorded failures rather than verified operating hours between failures. These metrics need improvement before they can be used for industrial reporting.

AI predictions are indicators for further investigation, not confirmation of an actual machine fault. Real deployment would require validated data, appropriate sensor integration, industrial safety procedures, and testing.

## Future Improvements

- Connect to real sensors or a PLC through a suitable industrial communication protocol.
- Record actual operating time and downtime.
- Improve MTBF and availability calculations.
- Develop a live dashboard with trend charts.
- Add automated reporting and validated maintenance thresholds.
- Evaluate model performance on representative real-world data.

## Author

Electrical and Telecommunication Engineering graduate interested in industrial automation, predictive maintenance, machine learning, and engineering systems integration.