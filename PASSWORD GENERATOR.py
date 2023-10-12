import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    # Define character sets based on complexity requirements
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special_chars else ""
    
    # Combine character sets as per complexity requirements
    characters = lowercase_letters + uppercase_letters + digits + special_chars
    
    # Check if there are characters to choose from
    if not characters:
        print("Complexity requirements too strict. Password cannot be generated.")
        return ""
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"
    
    password = generate_password(length, include_digits, include_special_chars)
    
    if password:
        print(f"Generated Password: {password}")
    else:
        print("No password generated due to strict complexity requirements.")

if __name__ == "__main":
    main()
