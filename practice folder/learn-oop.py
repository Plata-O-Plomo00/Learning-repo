class vehicle:

    def __init__(self, name):
        self.name = name
        # self.grade = grade
        # self.marks = marks
    
    def get_name(self):
        print(f"My name is {self.name}") 
    
    def set_name(self, name):
        self.name = name

        print(f"No, my name is {name}")

student_1 = vehicle("Ahmad")

print(student_1.get_name())
print(student_1.set_name("ali"))