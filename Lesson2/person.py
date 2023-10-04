# Define the parent class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, name is {self.name} and I am {self.age} years old.")

# Create child classes that inherit from Person
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self, subject):
        print(f"{self.name} is a student in grade {self.grade} and is studying {subject}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is a teacher who teaches {self.subject}.")

class Engineer(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def design(self):
        print(f"{self.name} is an engineer specializing in {self.specialization} and is designing a new project.")

class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def diagnose(self, patient_name):
        print(f"{self.name} is a doctor with a specialty in {self.specialty} and is diagnosing {patient_name}.")

# Create instances of child classes
student = Student("Alice", 15, 9)
teacher = Teacher("Mr. Smith", 35, "Math")
engineer = Engineer("Alex", 28, "Software Engineering")
doctor = Doctor("Dr. Johnson", 45, "Cardiology")

# Let the persons introduce themselves
student.introduce()
teacher.introduce()
engineer.introduce()
doctor.introduce()

# Use unique methods of each class
student.study("Science")
teacher.teach()
engineer.design()
doctor.diagnose("John")
