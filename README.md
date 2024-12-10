# Encryption Methods using Python

This repository explores various encryption methods implemented in Python, providing a comprehensive understanding of how they work and where they can be applied. Below is a brief introduction to each method:

---

## 1. **Hashing**
### How It Works:
Hashing is a one-way process that converts input data into a fixed-length hash value. It uses mathematical algorithms to generate a unique fingerprint for the data. Common algorithms include MD5, SHA-1, and SHA-256.

### Characteristics:
- **Irreversible**: Original data cannot be retrieved from the hash.
- **Deterministic**: The same input always produces the same hash.
- **Fast**: Designed for quick computation.

### Use Cases:
- Storing passwords securely (with added salt).
- Ensuring data integrity by comparing hash values.
- Generating unique identifiers for files or messages.

### Notes:
- Avoid older algorithms like MD5 or SHA-1 for cryptographic purposes due to vulnerabilities.
- For password hashing, use dedicated libraries like `bcrypt` or `argon2` instead of plain hash functions.

---

## 2. **Salted Hashing**
### How It Works:
Salted hashing enhances standard hashing by adding a unique random value (salt) to the input data before hashing. This ensures that the same input produces different hashes every time.

### Characteristics:
- **Prevents Rainbow Table Attacks**: By introducing randomness, precomputed hash attacks are rendered ineffective.
- **Unique Output**: Even identical passwords generate distinct hashes.

### Use Cases:
- Securing stored passwords in databases.
- Enhancing the security of systems vulnerable to brute-force attacks.

### Notes:
- Always store the salt alongside the hash to enable verification.
- Use a strong random generator (e.g., `os.urandom`) to create the salt.

---

## 3. **HMAC (Hash-based Message Authentication Code)**
### How It Works:
HMAC combines a cryptographic hash function with a secret key to produce a message authentication code (MAC). This ensures data integrity and authenticity.

### Characteristics:
- **Keyed Hash**: Requires a shared secret key.
- **Tamper Detection**: Ensures the message hasn’t been altered.
- **Algorithm-Agnostic**: Can work with any hash function (e.g., SHA-256).

### Use Cases:
- Verifying the integrity of messages in communication protocols.
- Authenticating API requests.
- Securely validating tokens in web applications.

### Notes:
- Both parties must securely share and store the secret key.
- The strength of HMAC depends on the hash function and key length.

---

## 4. **Symmetric Encryption**
### How It Works:
Symmetric encryption uses the same key for both encryption and decryption. Algorithms like AES (Advanced Encryption Standard) are widely used for this purpose.

### Characteristics:
- **Fast and Efficient**: Suitable for encrypting large datasets.
- **Single Key**: The same key must be shared securely between parties.

### Use Cases:
- Securing files and data at rest.
- Encrypting communication in trusted environments (e.g., VPNs).
- Protecting sensitive data in databases.

### Notes:
- Key management is critical; if the key is exposed, the data is vulnerable.
- Use authenticated encryption modes like GCM to prevent tampering.

---

## 5. **Asymmetric Encryption**
### How It Works:
Asymmetric encryption uses a key pair: a **public key** for encryption and a **private key** for decryption. Algorithms like RSA and ECC (Elliptic Curve Cryptography) are commonly used.

### Characteristics:
- **Key Pair**: Public key is shared, private key is kept secret.
- **Scalable**: Ideal for secure communication without pre-shared keys.
- **Resource-Intensive**: Slower compared to symmetric encryption.

### Use Cases:
- Securing sensitive data during transmission (e.g., HTTPS).
- Digital signatures for verifying authenticity.
- Key exchange in hybrid encryption systems.

### Notes:
- Asymmetric encryption is often combined with symmetric encryption (hybrid encryption) for better performance.
- Use sufficiently large key sizes (e.g., 2048-bit RSA) for strong security.

---

### Learn More
---
- Watch this: [7 Cryptography Concepts EVERY Developer Should Know](https://youtu.be/NuyzuNBFWxQ?si=7ManJszHRloAoMPl)
