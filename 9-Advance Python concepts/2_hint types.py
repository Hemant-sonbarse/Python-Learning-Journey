

age: int = 25  # 'age' is expected to be an integer
name: str = "Alice"  # 'name' is expected to be a string
is_active: bool = True  # 'is_active' is expected to be a boolean
height: float = 5.7  # 'height' is expected to be a float


def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Alice"))  # Output: Hello, Alice!
