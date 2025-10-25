from Class_Work_Task import *
from Class_Personal_Task import *
from datetime import datetime
class TaskManager :
    def __init__(self) :
        self.tasks = []
        # self.current_id = None

    def add_task(self,task) :
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks :
            if task.title == title :
                self.tasks.remove(task)
                print(f"Task '{title}' deleted successfully.")
                return True
        print("Task not found.")
        return False

    def update_due_date(self, title, new_date):
        for task in self.tasks:
            if task.title == title:
                if task.validate_date(new_date) :
                    task.due_date = new_date
                    print(f"Due date for '{title}' is updated.")
                    return True
                else:
                    return False
        print("the task not found.")
        return False

    def mark_task_complete(self, title) :
        for task in self.tasks :
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed.")
                return True
        print("Task not found.")
        return False

    def mark_task_inProgress(self, title):
        for task in self.tasks :
            if task.title == title:
                task.mark_inProgress()
                print(f"Task '{title}' marked as in progress.")
                return True
        print("Task not found.")
        return False

    def view_tasks(self, method=None):

        if not self.tasks :
            print("No tasks available.")

        else :
            temp_tasks = self.tasks.copy()
            if method == "creation" :
                temp_tasks.sort(key = lambda x : x.creation_time)
            elif method == "due_date":
                temp_tasks.sort(key=lambda x : x.due_date )
            elif method == "status" :
                temp2_tasks = []
                s = input("ُEnter the status (completed/in progress/incomplete) : ").lower().strip()
                if s == "completed" or s == "incomplete" or s == "in progress" :
                    for task in temp_tasks :
                        if task.status == s :
                            temp2_tasks.append(task)
                    temp_tasks = temp2_tasks
                else :
                    print("please take care the spelling")
                    return False
            elif method == "type" :
                temp2_tasks = []
                t = input("ُEnter the type (work,personal) and enter any thing else to general tasks : ").lower().strip()
                if t == "work" or t == "personal" :
                    for task in temp_tasks:
                        if task.type == t :
                            temp2_tasks.append(task)
                    temp_tasks = temp2_tasks
                else :
                    for task in temp_tasks:
                        if task.type == "general" :
                            temp2_tasks.append(task)
                    temp_tasks = temp2_tasks
            else :
                pass

            if temp_tasks :
                for i, task in enumerate(temp_tasks, start=1):
                    print(f"\n--- Task {i} ---")
                    task.display()
            else :
                print(f"\n--> Tasks not found.")

    def check_due_tasks(self):
        today_tasks = []
        current_date = datetime.now().date()
        for task in self.tasks:
            task_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
            if task_date == current_date :
                today_tasks.append(task)
        if today_tasks :
            print("\n--- Due Tasks Reminder ---")
            for task in today_tasks :
                print(f"Task '{task.title}' is due on today '{task.due_date}'")

    def read_json(self, data_list, ID):
        self.tasks = []
        # self.current_id = ID
        for task_data in data_list[ID]["tasks"] :
            if task_data["type"] == "personal":
                task = PersonalTask(task_data["title"], task_data["description"], task_data["due_date"],task_data["category"],task_data["type"],task_data["status"])
            elif task_data["type"] == "work":
                task = WorkTask(task_data["title"], task_data["description"], task_data["due_date"],task_data["priority"],task_data["type"],task_data["status"])
            else:
                task = Task(task_data["title"], task_data["description"], task_data["due_date"],task_data["type"],task_data["status"])
            self.tasks.append(task)

