class Employee:
    language = "Py"      #This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):   #dunder method which is automaticslly called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object ")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod     #it is a decorator
    def greet():
        print("Good morning")

hemant = Employee("Hemant", 1300000, "Javascript")
hemant.name = "Hemant"
print(hemant.name, hemant.salary, hemant.language)


hemant.greet()