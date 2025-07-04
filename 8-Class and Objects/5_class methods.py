class Employee:
    a = 1  # Class attribute

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()  # Create an instance
e.a = 45  # This creates an instance attribute, not modifying the class attribute

Employee.show()  # Still refers to the class attribute, so prints "1"
#e.show()