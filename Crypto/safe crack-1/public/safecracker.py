import base64

def password_checker(password, encoded_key):
    decoded_key = base64.b64decode(encoded_key).decode('utf-8')
    if password == decoded_key:
        return True
    else:
        return False

# Example usage:
encoded_key = "eGlhYWV3emwxMjNfYWVpbw=="
password = input("Enter password: ")

if password_checker(password, encoded_key):
    print("Password is correct!")
else:
    print("Incorrect password!")
