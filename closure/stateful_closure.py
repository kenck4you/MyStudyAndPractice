def make_counter(count=0):
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter(5)

print(my_counter())
print(my_counter())
