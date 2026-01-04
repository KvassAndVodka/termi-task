# Termi-Task

Project Link: [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

A simple, dependency-free command line task manager built with Python.

## Features
- **Add** tasks to a local list.
- **List** tasks (all, or filter by: todo, in-progress, done).
- **Update** task descriptions.
- **Delete** tasks.
- **Mark** tasks as in-progress or done.
- **Persists** data to `tasks.json` in the current directory.

## Requirements
- Python 3.x
- No external libraries required.

## Usage

### 1. Add a Task
```bash
python task-cli.py add "Buy groceries"
```
### 2. List Tasks:
```bash
python task-cli.py list
```

Filter by status:
```bash
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done
```

### 3. Update a Task
```bash
# Usage: update <id> <new_description>
python task-cli.py update 1 "Buy groceries and cook dinner"
```

### 3. Change Status
```bash
python task-cli.py mark-in-progress 1
python task-cli.py mark-done 1
# Optional: mark back to todo
python task-cli.py mark-to-do 1
```

### 5. Delete a Task
```bash
python task-cli.py delete 1
```