from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Securely store the key and IV, as they're needed for decryption.
# Losing them means the data cannot be decrypted.
key = os.urandom(32)
iv = os.urandom(16)

def message_encoder(msg):

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(msg) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

    return encrypted_message


def message_decoder(encrypted_msg):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_message = decryptor.update(encrypted_msg) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

    return decrypted_message.decode()



message = b"My name is Tom Marvolo Riddle"
encoded_message = message_encoder(message)
decoded_message = message_decoder(encoded_message)

print("Encrypted message:", encoded_message)
print("Decrypted message:", decoded_message)



