from datetime import datetime
class Task :
    def __init__(self, title, description, due_date, type="general",status="incomplete") :
        self.type = type
        self.title = title
        self.description = description
        self.due_date = self.validate_date(due_date)
        self.status = status
        self.creation_time = datetime.now()

    def validate_date(self, due_date) :
        try:
            date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
            current_date = datetime.now().date()
            if date_obj < current_date:
                print("This date is in the past, Please enter a future date.")
                return None
            return due_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")
            return None

    def mark_inProgress(self):
        self.status = "in progress"

    def mark_completed(self):
        self.status = "completed"

    def display(self) :
        print(f"Task title : {self.title}")
        print(f"Task description : {self.description}")
        print(f"Task due date : {self.due_date}")
        print(f"Task status : {self.status}")

    def to_dictionary (self) :
        return {
            "type" : self.type  ,
            "title" : self.title,
            "description" : self.description,
            "due_date" : self.due_date,
            "status" : self.status,
        }