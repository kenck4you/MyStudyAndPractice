def make_greeting(f_name, l_name):
    def return_greeting():
        return f"Hello, {f_name.title()} {l_name.title()}!"
    return return_greeting

hello_mary = make_greeting('mary', 'x')
hello_frank = make_greeting('frank', 'sinatra')

print(hello_mary())
print(hello_frank())