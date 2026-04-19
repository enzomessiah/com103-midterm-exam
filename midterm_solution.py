task_types = [
    ("Program Logic / Coding", 6),
    ("UI / Output Formatting", 3),
    ("Testing & Debugging", 2),
    ("Documentation / README", 2),
    ("Presentation Slides", 2)
    ]

project_title = input("Enter project title: ")
group_name = input("Enter group name: ")

print("==========================================")
print("   COM 103 PROJECT -- TASK TYPES")
print("==========================================")

for i, (task, hours) in enumerate(task_types, start=1):
    print(f" {i}. {task:<30} [{hours}h]")

print("==========================================")

assignments = []
total_points = 0


for i in range(1, 5):
    print(f"--- TASK {i} ---")
    
    task_num = int(input("Task number (0 to skip): "))

    if task_num == 0:
        continue

    if 1 <= task_num <= 5:
        
        member = input("Member name: ")
        
        
        while True:
            status = input("Status (done/pending): ").lower()
            if status in ["done", "pending"]:
                break
            print("Invalid input. Please enter 'done' or 'pending'.")

        
        points = 2 if status == "done" else 1
        total_points += points

        task_name, hours = task_types[task_num - 1]

        assignments.append({
            "task_name": task_name,
            "hours": hours,
            "member": member,
            "status": status,
            "points": points
        })
    else:
        print("Invalid task number. Skipping...")


assigned_count = len(assignments)
max_points = assigned_count * 2

progress = int((total_points / max_points) * 100) if max_points > 0 else 0


if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"


print("================================================")
print(f"     {project_title} -- TASK BOARD")
print("================================================")
print(f"Group Name: {group_name}")

for i, task in enumerate(assignments, start=1):
    print(f"{i}. {task['task_name']} [{task['hours']}h]")
    print(f"   Member: {task['member']}")
    print(f"   Status: {task['status']}")
    print(f"   Points: {task['points']}")

print("------------------------------------------------")
print(f"Total Points: {total_points}")
print(f"Progress: {progress}%")
print(f"Project Status: {project_status}")
print(" ")
print("================================================")
print("     Canteen Ordering System -- TASK BOARD")
print("================================================")