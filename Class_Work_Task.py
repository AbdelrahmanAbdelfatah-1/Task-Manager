from Class_Task import Task

class WorkTask(Task) :
    def __init__(self, title, description, due_date , priority, type="general",status="incomplete") :
        super().__init__(title, description, due_date ,type,status)
        self.priority = priority
    def to_work_dictionary (self) :
        data = super().to_dictionary()
        data["priority"] = self.priority
        data["type"] = self.type
        return data
    def display(self) :
        print(f"Task type : {self.type}")
        super().display()
        print(f"Task priority : {self.priority}")
