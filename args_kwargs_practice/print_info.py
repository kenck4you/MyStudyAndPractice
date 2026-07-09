def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_info(name='Mary', age=20, city='Los Angeles')
