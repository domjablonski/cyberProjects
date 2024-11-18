import re
import string

COMMON_PASSWORDS = {"password", "123456", "123456789", "qwerty", "abc123", "password123", "letmein", "admin", "welcome"}

def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short. Must be at least 8 characters."
    
    if password.lower() in COMMON_PASSWORDS:
        return "Password is too common. Please choose a more secure password."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    if re.search(r"(.)\1{2,}", password):
        return "Password should not contain 3 or more consecutive identical characters."

    for word in COMMON_PASSWORDS:
        if word in password.lower():
            return f"Password contains a common word: {word}. Choose a more unique password."

    if re.search(r"123456|abcdef|qwerty|asdfgh", password.lower()):
        return "Password should not contain easily guessable sequences like '123456' or 'abcdef'."

    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and 
            re.search(r"\d", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return "Password should have a good mix of uppercase letters, lowercase letters, digits, and special characters."

    return "Password is strong."

def get_valid_password():
    while True:
        password = input("Enter a password to check: ")
        result = check_password_strength(password)
        print(result)
        
        if result == "Password is strong.":
            break

get_valid_password()

