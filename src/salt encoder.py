import hashlib
import os

def password_encoder(password):
    salt = os.urandom(16)
    password = password.encode()

    salted_password = salt + password

    hash_object = hashlib.sha256(salted_password)
    hashed_value = hash_object.hexdigest()

    return hashed_value


password = "123456"
encoded_password_1 = password_encoder(password)
encoded_password_2 = password_encoder(password)

print("Salted Hash:", encoded_password_1)
print("Salted Hash:", encoded_password_2)

