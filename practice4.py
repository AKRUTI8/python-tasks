class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print(self.role,self.dept,self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Enginner","AIML","40000")

e1 = Engineer("Elon musk",40)
e1.showDetails()