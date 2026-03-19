import random
import string

def generate_password(length=12):
    # Combine all character types
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
print("Generated Password:", generate_password(12))
