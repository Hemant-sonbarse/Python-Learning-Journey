class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        if len(new_name) < 3:
            raise ValueError("Name must be at least 3 characters long!")
        self._name = new_name

# Creating an object
p = Person("John")

# Using the getter (looks like an attribute)
print(p.name)  # Output: John

# Using the setter
p.name = "Alex"  # ✅ Works
print(p.name)  # Output: Alex

# Trying to set an invalid name
# p.name = "Al"  # ❌ Raises ValueError
