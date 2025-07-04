class Employee:
    language = "Py"      #This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod     #it is a decorator
    def greet():
        print("Good morning")

hemant = Employee()
hemant.name = "Hemant"   #This is a object (instance) attribute
print(hemant.name, hemant.salary, hemant.language)


hemant.getInfo()
Employee.getInfo(hemant)



hemant.greet()