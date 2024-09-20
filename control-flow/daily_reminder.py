task = input("Enter task description: ")
priority = input("Enter priority level (high, medium, low): ")
time_bound = input("Is the task time-bound? (y/n): ")

match priority:
    case 'high':
        if time_bound == 'y':
            print(f"'{task}' is a high priority task that requires immediate attention today.")
        else:
            print(f"'{task}' is a high priority task. Consider completing it when you have free time.")
    case 'medium':
        if time_bound == 'y':
            print(f"'{task}' is a medium priority task that requires immediate attention today.")
        else:
            print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
    case 'low':
        if time_bound == 'y':
            print(f"'{task}' is a low priority task that requires immediate attention today.")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
