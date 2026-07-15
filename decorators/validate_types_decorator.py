import functools

def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args):
        for arg in args:
            if type(arg) != int and type(arg) != float:
                raise TypeError(f"Аргумент {arg} не прошёл валидацию")
        res = func(*args)
        return res
    return wrapper

@validate_types
def squares(*args):
    return [x**2 for x in args]

print(squares(4, 9, 16, 25, 36, 49))
print(squares(4, 9, 16, '25', 36))
