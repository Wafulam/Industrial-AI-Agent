
from tools import check_motor, generate_report
from motor_ai import predict_motor
from history import save_reading, analyze_history
from machine_runtime import start_machine, stop_machine, show_runtime
from maintenance_summary import update_maintenance_summary
from maintenance_metrics import (
    record_failure,
    record_repair,
    show_mttr,
    show_mtbf,
    show_availability
)
from excel_logger import (
    save_to_excel,
    save_alert_to_excel,
    show_alert_history
)

print("======================================")
print("     INDUSTRIAL MAINTENANCE AGENT")
print("======================================")

last_motor_data = None
last_condition = None
last_recommendation = None
last_confidence = None


while True:
    user_input = input("\nYou: ").lower().strip()

    # Check motor condition using AI
    if user_input == "check motor":
        print("\nAgent: Collecting motor readings...")

        last_motor_data = check_motor()
        result = predict_motor(last_motor_data)

        last_condition = result["condition"]
        last_confidence = result["confidence"]
        last_recommendation = result["recommendation"]

        # Save readings to CSV history
        save_reading(last_motor_data, last_condition)

        # Save readings and prediction to Excel
        save_to_excel(
            last_motor_data,
            last_condition,
            last_confidence,
            last_recommendation
        )

        print("\n--- AI MOTOR ANALYSIS ---")
        print(f"Predicted condition: {last_condition}")

        print("\nPrediction confidence:")
        for condition, probability in last_confidence.items():
            print(f"{condition}: {probability}%")

        print(f"\nAgent: {last_recommendation}")
         
       
        if last_condition == "Fault":
            alert_message = (
                "High-priority alert: motor fault predicted. "
                "Arrange an inspection and follow site safety procedures."
            )
            print("\n🚨 ALERT: MOTOR FAULT PREDICTED!")
            print(alert_message)
            save_alert_to_excel("Fault", alert_message)

        elif last_condition == "Warning":
            alert_message = (
                "Abnormal motor condition predicted. "
                "Inspect the motor and monitor its readings."
            )
            print("\n⚠️ WARNING: ABNORMAL MOTOR CONDITION PREDICTED!")
            print(alert_message)
            save_alert_to_excel("Warning", alert_message)

        else:
            print("\nMotor condition predicted as NORMAL.")



    # View motor history
    elif user_input == "history":
        analyze_history()

    # Generate motor maintenance report
    elif user_input == "report":
        if last_motor_data is None:
            print("Agent: Please run 'check motor' first.")
        else:
            generate_report(
                last_motor_data,
                last_condition,
                last_recommendation,
                last_confidence
            )

    # Machine runtime tracking
    elif user_input == "start machine":
        start_machine()

    elif user_input == "stop machine":
        stop_machine()

    elif user_input == "runtime":
        show_runtime()

    # Confirmed breakdown and repair tracking
    elif user_input == "record failure":
        record_failure()

    elif user_input == "record repair":
        record_repair()

    elif user_input == "mttr":
        show_mttr()

    elif user_input == "availability":
        show_availability() 
    
    elif user_input == "summary":
        update_maintenance_summary()    

    elif user_input == "mtbf":
        show_mtbf()
    
    elif user_input == "alerts":
        show_alert_history()

    # Exit the agent
    elif user_input == "exit":
        print("Agent: Goodbye!")
        break

    # Help message
    else:
        print(
            "\nAgent: Available commands:\n"
            "- check motor\n"
            "- history\n"
            "- report\n"
            "- start machine\n"
            "- stop machine\n"
            "- runtime\n"
            "- record failure\n"
            "- record repair\n"
            "- mttr\n"
            "- mtbf\n"
            "- availability\n"
            "- summary\n"
            "- alerts\n"
            "- exit"
        )
