from collections import deque

tasks = deque()


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("task added.")
    
    
def execute_task():
    if not tasks:
        print("no tasks availble.")
    else:
        task = tasks.popleft()
        print("Executing:", task)
        
                
def view_tasks():
    
    if not tasks:
        print("No tasks.")
        
    else:
        print("Pending Tasks:")
        
        for task in tasks:
            print("-", task)
            
            
while True:
    
    print("\n--- TASK SCHEDULER ---")
    print("1. Add Task")
    print("2. Execute Task")
    print("3. View Task")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_task()
        
    elif choice == "2":
        execute_task()
        
    elif choice == "3":
        execute_task()                                        
        
    elif choice == "4":
        break    