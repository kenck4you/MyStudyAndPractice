def create_user(username, *args, **kwargs):
    print(f"Username: {username}")
          
    print(f"\n{username} hobbies:")
    for hobby in args:
        print(f"- {hobby}")

    print(f"\nAdditional info:")
    for k, v in kwargs.items():
        print(f"{k}: {v}")

create_user('mary', 'travels', 'hobbyhorsing', 'vororephilia', age=20, city='Los Angeles', country='USA')