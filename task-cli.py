import sys
import os
import json
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    else:
        return []


def save_task(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(description):
    tasks = load_tasks()
    if not tasks:
        new_id = 1
    else:
        new_id = max(t["id"] for t in tasks) + 1
    
    now = datetime.now().isoformat()

    new_tasks = {
        "id": new_id,
        "description": description,
        "status": "to-do",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_tasks)
    save_task(tasks)

    print(f"Task ID:{new_id} has been addded successfully!")

def update_task(task_id, description):
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == int(task_id):
            t["description"] = description
            t["updatedAt"] = datetime.now().isoformat()
            found = True
            break

    if found:
        save_task(tasks)
        print(f"Task ID: {task_id} has been updated successfully!")
    else:
        print(f"Task ID: {task_id} is not found.")


def mark_task(task_id, new_status):
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == int(task_id):
            t["status"] = new_status
            t["updatedAt"] = datetime.now().isoformat()
            found = True
            break

    if found:
        save_task(tasks)
        print(f"Task ID: {task_id} status has been updated!")
    else:
        print(f"Task ID: {task_id} is not found.")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != int(task_id)]
    
    if len(tasks) == len(new_tasks):
        print(f"Task ID: {task_id} is not found.")
    else:
        save_task(new_tasks)
        print(f"Task ID: {task_id} has been deleted successfully!")


def list_tasks(status):
    tasks = load_tasks()

    if status:
        tasks = [t for t in tasks if t["status"] == status]
    
    if not tasks:
        print("No tasks found.")
        return
    
    header = f"{'ID':<5} {'Description':<40} {'Status':<15} {'Created at':<40}"
    print(header)
    print("-" * len(header))

    for t in tasks:
        date_str = t['createdAt'][:19]
        print(f"{t['id']:<5} {t['description']:<40} {t['status']:<15} {date_str:<20}")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description")
            return
        if len(sys.argv) > 3:
            print("Error: Too many arguments")
            return
        
        add_task(sys.argv[2])

    elif command == "list":
        if len (sys.argv) < 2:
            print("Error: Command is invalid.")
            return
        if len (sys.argv) > 3: 
            print("Error: Too many arguments")
            return

        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Missing arguments for update (id, description)")
            return
        if len(sys.argv) > 4:
            print("Error: Too many arguments")
            return

        update_task(sys.argv[2], sys.argv[3])
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task ID for delete.")
            return
        if len(sys.argv) > 3:
            print("Error: Too many arguments")
            return
        delete_task(sys.argv[2])

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Argument is too short.")            
            return
        if len(sys.argv) > 3:
            print("Error: Too many arguments")
            return
        mark_task(sys.argv[2], "in-progress")

    elif command == "mark-to-do":
        if len(sys.argv) < 3:
            print("Error: Argument is too short.")           
            return
        if len(sys.argv) > 3:
            print("Error: Too many arguments")
            return
        mark_task(sys.argv[2], "to-do")
          
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error")                     
            return
        if len(sys.argv) > 3:
            print("Error: Too many arguments")
            return
        mark_task(sys.argv[2], "done")

    else:
        print(f"Unknown command: {command}")
        

if __name__ == '__main__':
    main()