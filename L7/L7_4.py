from datetime import datetime

def logs_func(func):
    start = datetime.now()
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function name: {func.__name__}, Expected: {func.__annotations__}, time start: {start}, lead time {datetime.now() - start}, input: {args}, result: {result}")
        return result
    return wrapper


@logs_func
def test(a:int, b:str):
    return(f'{a} {b}')


x = test(5,'street')
print(f'{x} <- is not wrapper')