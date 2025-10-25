from Class_Task import Task
class PersonalTask(Task) :
    def __init__(self, title, description, due_date , category, type="general",status="incomplete") :
        super().__init__(title, description, due_date , type , status)
        self.category = category
    def to_personal_dictionary (self) :
        data = super().to_dictionary()
        data["type"] = self.type
        data["category"] = self.category
        return data
    def display(self) :
        print(f"Task type : {self.type}")
        super().display()
        print(f"Task category : {self.category}")
