def is_palindrome(text):
    if len(text) in [1, 0]:
        return True
    if text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1: -1])

print(is_palindrome('level'))
print(is_palindrome(''))
print(is_palindrome('a'))
print(is_palindrome('hello'))
print(is_palindrome('aboba'))
print(is_palindrome('jnujbbhbhb'))