import datetime

# 🧾 Decorator to log operations
def log_operations(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"[{datetime.datetime.now()}] Operation: {func.__name__} with args: {args}")
            result = func(*args, **kwargs)
            print(f"[{datetime.datetime.now()}] Result: {result}")
            return result
        except Exception as e:
            print(f"[{datetime.datetime.now()}] Error: {str(e)}")
            return None
    return wrapper

# 💡 Closure to keep memory of last result
def calculator():
    memory = {"value": 0}

    @log_operations
    def add(x):
        memory["value"] += x
        return memory["value"]

    @log_operations
    def subtract(x):
        memory["value"] -= x
        return memory["value"]

    @log_operations
    def multiply(x):
        memory["value"] *= x
        return memory["value"]

    @log_operations
    def divide(x):
        if x == 0:
            raise ValueError("Cannot divide by zero!")
        memory["value"] /= x
        return memory["value"]

    @log_operations
    def reset():
        memory["value"] = 0
        return memory["value"]

    return add, subtract, multiply, divide, reset

# 🎯 Main Execution
if __name__ == "__main__":
    add, subtract, multiply, divide, reset = calculator()

    add(10)
    multiply(2)
    subtract(5)
    divide(3)
    reset()
