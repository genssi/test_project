from datetime import datetime
from functools import wraps

def timer(func):
    @wraps(func)
    def time_zone(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        res = end - start
        return print(f'{func(*args, **kwargs)}\nВремя выполнения: {res}')
    return time_zone

        

@timer
def fizz_buzz(num):
    for x in num:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)
            
fizz_buzz = fizz_buzz(range(1, 101))