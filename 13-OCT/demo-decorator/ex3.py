import time

def slow_function():
    time.sleep(5)
    return "Operation Completed"

res = slow_function()
print(res)