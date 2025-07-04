class Employee:
    language = "Py"      #This is a class attribute
    salary = 1200000

hemant = Employee()
hemant.language = "Javascript"   #This is a object (instance) attribute
print(hemant.salary, hemant.language)
