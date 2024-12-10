from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_key_pair(show_keypairs=False):
    
    # The public key is the lock that anyone can use to secure (encrypt) data.
    # The private key is the unique key that unlocks (decrypts) the data.
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        )

    public_key = private_key.public_key()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
        )

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    if show_keypairs:
        print("Private Key:\n", private_key_pem.decode())
        print("Public Key:\n", public_key_pem.decode())

    return public_key, private_key


def message_encoder(msg, public_k):
    ciphertext = public_k.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return ciphertext


def message_decoder(cipher_t, private_k):
    plaintext = private_k.decrypt(
        cipher_t,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext


public_key, private_key = generate_key_pair()

message = b"My name is Tom Marvolo Riddle"
encoded_message = message_encoder(message, public_key)
decoded_message = message_decoder(encoded_message, private_key)

print("Encrypted message:", encoded_message)
print("Decrypted message:", decoded_message.decode())

