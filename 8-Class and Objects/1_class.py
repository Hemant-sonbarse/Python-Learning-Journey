class Employee:
    language = "Py"      #This is a class attribute
    salary = 1200000

hemant = Employee()
hemant.name = "Hemant"   #This is a object (instance) attribute
print(hemant.name, hemant.salary, hemant.language)

rohan = Employee()
rohan.name = "Rohan robinson"
print(rohan.name, rohan.language, rohan.salary)

# Here name is object attribute and salary and language are class
# attributes as they directly belong to the class