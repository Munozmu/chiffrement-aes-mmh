def generate_keystream(key, length):
    """Génère une séquence pseudo-aléatoire (keystream) en utilisant XOR."""
    keystream = []
    key = [ord(char) for char in key]  # Convertit la clé en une liste d'entiers
    key_length = len(key)
    
    for i in range(length):
        # Utilise XOR pour combiner les octets de la clé de manière cyclique
        keystream.append(key[i % key_length])
    
    return keystream

def encrypt(message, keystream):
    """Chiffre un message en utilisant XOR avec le keystream."""
    encrypted_message = [message[i] ^ keystream[i] for i in range(len(message))]
    return encrypted_message

def decrypt(encrypted_message, keystream):
    """Déchiffre un message en utilisant XOR avec le keystream."""
    decrypted_message = [encrypted_message[i] ^ keystream[i] for i in range(len(encrypted_message))]
    return decrypted_message

# Exemple avec un truc concret
message = "Hello, World!"
key = "secretkey"

# Générer le keystream
keystream = generate_keystream(key, len(message))

# Convertir le message en une liste d'entiers
message_int = [ord(char) for char in message]

# Chiffrer le message
encrypted_message = encrypt(message_int, keystream)
print("Message chiffré:", ''.join([str(char) for char in encrypted_message]))

# Déchiffrer le message
decrypted_message = decrypt(encrypted_message, keystream)
print("Message déchiffré:", ''.join([chr(char) for char in decrypted_message]))