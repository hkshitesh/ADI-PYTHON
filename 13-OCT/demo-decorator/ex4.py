import time

def time_decorator(func):
    def wrapper():
        start_time= time.time()
        result = func()
        end_time = time.time()
        print(f"time taken by {func.__name__} : {end_time-start_time: .5f} seconds")
        return result
    return  wrapper


@time_decorator
def slow_function():
    time.sleep(5)
    return "Operation Completed"

res = slow_function()
print(res)