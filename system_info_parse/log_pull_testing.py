import subprocess
import json

def get_logs():
    #First I will define the log command to fetch my logs
    command = [
        #adding sudo as the logs are not parsing
        "sudo", "log", "show",
        "--predicate", '(eventType == "logEvent" && (messageType == "Error" || messageType == "Fault"))', 
        "--style", "json",
        "--last", "1h" #I will modify the time frame as needed
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        log_entries = [json.loads(line) for line in result.stdout.strip().split('\n') if line]

        with open('critical_logs.json', 'w') as f:
            json.dump(log_entries, f, indent=4)

        print("Critical logs have been saved to 'critical_logs.json'.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing log command: {e}")
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON output: {e}")

get_logs()