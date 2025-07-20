# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to process priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority level"

# Adjust message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Note" not in message:
        message += ". Try to complete it as soon as possible."
    else:
        message += ". Consider completing it when you have free time."

# Output the final reminder
print("\n" + message)
