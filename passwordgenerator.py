import secrets
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define the character sets to use in the password
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a secure random password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)
