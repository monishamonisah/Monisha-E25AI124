# Password Strength Checker Skeleton Program

def check_password_strength(password):
    """
    Function to check the strength of a given password.
    Criteria can include length, uppercase, lowercase, digits, special characters, etc.
    """
    strength = 0
    
    # Check if password length is sufficient
    if len(password) >= 8:
        strength += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    
    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        strength += 1
    
    return strength

def main():
    # Input from user
    password = input("Enter your password: ")
    
    # Check password strength
    strength = check_password_strength(password)
    
    # Output result
    if strength >= 4:
        print("Strong password")
    elif strength == 3:
        print("Moderate password")
    else:
        print("Weak password")

if __name__== "__main__":
    main()
