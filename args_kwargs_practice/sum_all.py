def sum_all(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_all(1, 2, 3))
print(sum_all(10, 20))
print(sum_all())