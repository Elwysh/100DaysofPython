# Code answer to the exercise in the course

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
    
    def wrapper_func():
        before_time = time.time()                                  # code that runs before the called function
        func()                                                     # the called function
        after_time = time.time()                                   # code that runs after the called function
        runtime = after_time - before_time
        print(f"{func.__name__} run speed: {runtime}s")
    
    return wrapper_func

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()
