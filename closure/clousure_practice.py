def make_counter(count=0):
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def decorator(func):
    def wrapper():
        c = func()
        print('Счет:', c)
    return wrapper

my_count = make_counter()
test_decorator = decorator(my_count)

for i in range(5):
    test_decorator()