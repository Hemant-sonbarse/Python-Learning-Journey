from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
print(f"Numbers List: {numbers}")

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
print(f"Person Tuple: {person}")

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
print(f"Scores Dictionary: {scores}")

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
print(f"Initial Identifier: {identifier}")

# Reassigning with an integer (valid because of Union)
identifier = 12345
print(f"Updated Identifier: {identifier}")
