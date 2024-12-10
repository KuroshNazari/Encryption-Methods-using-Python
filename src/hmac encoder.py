import hmac
import hashlib 


def password_encoder(msg, key):
    return hmac.new(key, msg, hashlib.sha256).hexdigest()

password = b"My name is Tom Marvolo Riddle"

msg_1 = password_encoder(b"keyword", password)
msg_2 = password_encoder(b"newkeyword", password)

print(f"HMAC encrypted password using key 1: {msg_1}")
print(f"HMAC encrypted password using key 2: {msg_2}")