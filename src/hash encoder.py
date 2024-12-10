import hashlib

# SHA-256: Secure and widely used (recommended for most use cases).
# SHA-1: Older and less secure (not recommended for new projects).
# MD5: Fast but insecure for cryptographic purposes.

def password_encoder(psword, algorithm='sha256'):
    encoded_data = psword.encode()

    if algorithm == 'sha256':
        hash_object = hashlib.sha256(encoded_data)
    elif algorithm == 'sha1':
        hash_object = hashlib.sha1(encoded_data)
    elif algorithm == 'md5':
        hash_object = hashlib.md5(encoded_data)
    
    hash_hex = hash_object.hexdigest()

    return hash_hex


password = "My name is Tom Marvolo Riddle"
encoded_password = password_encoder(password, 'sha256')


print("Encrypted Password:", encoded_password)
