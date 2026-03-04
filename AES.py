import binascii
import base64
import hashlib
import secrets

from Cryptodome.Cipher import AES
from Cryptodome import Random

# This separator is used to join the encryption key text
# and the encrypted message text into one combined string.

TEXT_SEPARATOR = ":"


def generate_random_key():
    """
    Create a strong encryption key.

    A set of random bytes is created, and then sent through
    SHA-256. This produces a clean and consistent thirty-two byte 
    key that can be used with the Advanced Encryption Standard.
    """
    
    random_bytes = secrets.token_bytes(32)
    strong_key = hashlib.sha256(random_bytes).digest()
    return strong_key


def encrypt(plain_text_message):
    """
    Encrypt a text message without using a user password.

    Steps:
    1. A new strong encryption key is created.
    2. A new Initialization Vector is created.
    3. The plain text message is encrypted using the Advanced 
       Encryption Standard.
    4. The Initialization Vector and the encrypted bytes
       are combined and turned into hexadecimal text.
    5. The encryption key is turned into Base64 text.
    6. Both pieces are joined into one text string.
    """

    encryption_key = generate_random_key()
    initialization_vector = Random.new().read(AES.block_size)

    cipher_object = AES.new(encryption_key, AES.MODE_CFB, initialization_vector)
    encrypted_bytes = cipher_object.encrypt(plain_text_message.encode("utf-8"))

    combined_bytes = initialization_vector + encrypted_bytes
    combined_hex_text = binascii.hexlify(combined_bytes).decode("utf-8")

    key_text = base64.b64encode(encryption_key).decode("utf-8")

    final_output = key_text + TEXT_SEPARATOR + combined_hex_text
    return final_output


def decrypt(combined_message_text):
    """
    Decrypt a message created by the encrypt function.

    Steps:
    1. Separate the encryption key text and the encrypted message text.
    2. Convert the encryption key text from Base64 into bytes.
    3. Convert the encrypted message text from hexadecimal into bytes.
    4. Extract the Initialization Vector and the encrypted part.
    5. Use the same key and Initialization Vector to recreate the
       Advanced Encryption Standard object.
    6. Decrypt the encrypted bytes back into a plain text message.
    """

    key_text, encrypted_hex = combined_message_text.split(TEXT_SEPARATOR, 1)

    encryption_key = base64.b64decode(key_text.encode("utf-8"))
    encrypted_bytes = binascii.unhexlify(encrypted_hex.encode("utf-8"))

    initialization_vector = encrypted_bytes[:AES.block_size]
    encrypted_part = encrypted_bytes[AES.block_size:]

    cipher_object = AES.new(encryption_key, AES.MODE_CFB, initialization_vector)
    plain_bytes = cipher_object.decrypt(encrypted_part)

    return plain_bytes.decode("utf-8", errors="replace")
