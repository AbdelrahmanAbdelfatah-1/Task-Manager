from Class_Task_Manager import *
from Class_Personal_Task import *
from Class_Work_Task import *
import json
try:
    file = open("Data.json", "r")
    Data = json.load(file)
    file.close()
except:
    Data = []

manager = TaskManager()
def check_continuity():
    y = input("would you like to try again? write yes if you want to continue and write nothing to exit: ").lower()
    if y == "yes":
        return True
    else:
        return False
def check_id():
    try:
        ID = int(input("Enter ID : "))
        if ID < 0 :
            print("Please enter positive number.")
            if check_continuity() :
                return "continue"
            else :
                return "break"
        _ = Data[ID]
        return ID
    except ValueError:
        print("Invalid ID please enter a number .")
        if check_continuity():
            return "continue"
        else:
            return "break"
    except IndexError:
        print("ID not found!")
        if check_continuity():
            return "continue"
        else:
            return "break"
def write_json():
    with open("Data.json", "w") as f:
        json.dump(Data, f, indent=4)
def task_manager_menu(ID) :

    manager.read_json(Data,ID)
    manager.check_due_tasks()

    while True:

        print("\n################ Task Manager Menu ################\n")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Update Due Date")
        print("5. change the task status")
        print("6. Quit")

        choice = input("Enter the number of choice : ")

        if choice == "1" :

            print("\n######### Add New Task #########")

            task_type = input("Enter task type (personal/work) and and any thing else will be general type : ").lower().strip()
            while True :
                f = False
                fl = False
                title = input("Enter task title: ")
                for task in Data[ID]["tasks"]:
                    if task["title"] == title :
                        print("this title is already taken")
                        f = True
                if f :
                    if check_continuity() :
                        continue
                    else :
                        fl = True
                        break
                else :
                    break
            if fl :
                continue
            description = input("Enter task description : ")

            while True:

                flag = False

                temp_due_date = input("Enter due date in format (YYYY-MM-DD): ").strip()
                temp_task = Task(title, description, temp_due_date)

                if temp_task.due_date :
                    due_date = temp_due_date
                    break
                else:
                    if check_continuity():
                       continue
                    else:
                        flag = True
                        break
            if flag :
                continue

            if task_type == "personal" :
                category = input("Enter category (family, sports, etc.): ")
                task_obj = PersonalTask(title, description, due_date, category,task_type)
                task_dic = task_obj.to_personal_dictionary()

            elif task_type == "work":
                priority = input("Enter priority (high/medium/low): ")
                task_obj = WorkTask(title, description, due_date, priority,task_type)
                task_dic = task_obj.to_work_dictionary()

            else:
                task_type = "general"
                task_obj = Task(title, description, due_date,task_type)
                task_dic = task_obj.to_dictionary()

            manager.add_task(task_obj)
            Data[ID]["tasks"].append(task_dic)
            write_json()
            print("Task added successfully!")

        elif choice == "2":
            print("\n######### Delete Task #########")
            p = input("would you like to print the all tasks titles ? 'yes' for print all tasks and write nothing to enter the title : ").lower().strip()
            if p == "yes" :
                for i,task in enumerate ( Data[ID]["tasks"] , start = 1 ) :
                    print(f"{i}- '{task["title"]}'")
            while True :
                Title = input("Please enter the task title you want to delete : ").strip()
                if manager.delete_task(Title):
                    for task in Data[ID]["tasks"]:
                        if task["title"] == Title :
                            Data[ID]["tasks"].remove(task)
                            write_json()
                            break
                    break
                else :
                    if check_continuity() :
                        continue
                    else :
                        break

        elif choice == "3":

            print("\n######### Show Tasks #########")
            print("How would you like to view the tasks?")
            print("1. By creation order")
            print("2. By due date")
            print("3. By the status")
            print("4. By the type")

            while True :

                sort_choice = input("Enter the number of your choice (1-4) and enter any thing else if you need default way: ").strip()
                if sort_choice == "1":
                    manager.view_tasks("creation")
                    break
                elif sort_choice == "2":
                    manager.view_tasks("due_date")
                    break
                elif sort_choice == "3":
                    if manager.view_tasks("status") == False :
                        if check_continuity() :
                            continue
                        else :
                            break
                    else :
                        break
                elif sort_choice == "4":
                    manager.view_tasks("type")
                    break
                else:
                    print("showing tasks in default order.")
                    manager.view_tasks()
                    break

        elif choice == "4" :
            print("\n######### Update Due Date #########")
            p = input("would you like to print the all tasks titles with due date ? 'yes' for print all tasks and write nothing to enter the title : ").lower().strip()
            if p == "yes" :
                for i, task in enumerate(Data[ID]["tasks"], start=1):
                    print(f"{i}- '{task["title"]}' with due date '{task['due_date']}'")
            while True :
                Title = input("Please enter the task title you want to update : ").strip()
                due_date = input("Please enter the due date (YYYY-MM-DD): ").strip()
                if manager.update_due_date(Title, due_date):
                    for task in Data[ID]["tasks"] :
                        if task["title"] == Title :
                            task["due_date"] = due_date
                            write_json()
                            break
                    break
                else :
                    if check_continuity() :
                        continue
                    else :
                        break

        elif choice == "5" :
            print("\n######### Change Task Status #########")
            p = input("would you like to print the all tasks titles ? 'yes' for print all tasks and write nothing to enter the title : ").lower().strip()
            if p == "yes":
                for i, task in enumerate(Data[ID]["tasks"], start=1):
                    print(f"{i}- '{task["title"]}' with status '{task['status']}'")
            while True :
                Title = input("Please enter the task title : ").strip()
                status = input("Please enter the new task status (completed/in progress) : ").lower().strip()
                if status == "completed" :
                    if manager.mark_task_complete(Title) :
                        for task in Data[ID]["tasks"] :
                            if task["title"] == Title :
                                task["status"] = status
                                write_json()
                                break
                        break
                    else :
                        if check_continuity() :
                            continue
                        else :
                            break
                elif status == "in progress" :
                    if manager.mark_task_inProgress(Title) :
                        for task in Data[ID]["tasks"] :
                            if task["title"] == Title :
                                task["status"] = status
                                write_json()
                                break
                        break
                    else :
                        if check_continuity() :
                            continue
                        else:
                            break
                else :
                    print("please enter the right input and be careful with spelling")
                    if check_continuity() :
                        continue
                    else :
                        break

        elif choice == "6" :
            x = input("please leave us a comment if you faced any problems with the services we provide, if there is no comments enter '*' : ").strip()
            if x == "*" or x=="":
                print("\nI wish you a happy day")
                return "_"
            else :
                Data[ID]["rating"].append(x)
                write_json()
                print("\nI wish you a happy day")
                return "_"

        else :
            print("Invalid choice entered. Please try again.")

while True :

    print("\n############ Welcome to Task Manager ############\n")
    print("If you already have an account please enter login ")
    print("If you do not have an account please enter sign up ")
    print("Enter exit if you need to exit")

    x = (input("▶️ ").lower()).strip()

    if x == "login" :

        print( "\n############ ًWelcome to login page ############\n" )
        while True :
            ID = check_id()
            if ID == "continue"  :
                continue
            if ID == "break" :
                break
            password = input("Enter password : ")
            if Data[ID]["Password"] == password :
                print(f"\n=========== Welcome {Data[ID]["name"]} ===========")
                res = task_manager_menu(ID)
                if res == "_":
                    break
            else :
                print("Password incorrect!")
                y = input("would you like to try again, write yes if you want to continue and write nothing to exit: ").lower()
                if y == "yes":
                    continue
                else:
                   break

    elif x == "sign up" :

        print("############ Welcome to sign up page ############")

        name  = input("Enter your name : ")
        email = input("Enter your email : ")
        Password = input("Enter your password : ")
        confirm_password = input("Confirm your password : ")
        if Password != confirm_password:
            print("Passwords do not match ")
            continue
        ID = len(Data)

        User_Data = {
            "ID": ID ,
            "name": name ,
            "email": email,
            "Password": Password ,
            "tasks": [] ,
            "rating" : []
        }

        Data.append(User_Data)
        write_json()

        print(f"Sign in successful, Your ID is {ID}")
        print("You will Go to the main page to login and use our services ")
        print()

    elif x == "exit" :
        print("############ Goodbye I wish you a happy day ############")
        break

    else:
        print("Wrong data please try again")