import re

def text_checker(text):
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in text):
        return "unsafe"

    # Check for at least one lowercase letter
    if not any(char.islower() for char in text):
        return "unsafe"

    # Check for at least one digit
    if not any(char.isdigit() for char in text):
        return "unsafe"

    # Check for at least one special character (except space)
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', text):
        return "unsafe"

    # Check for minimum length of 8
    if len(text) < 8:
        return "unsafe"

    else:
        return "Safe"

user_input = input("Enter text to check: ")
result = text_checker(user_input)
print(result)
