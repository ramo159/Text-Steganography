import sys
sys.path

from embed import embedFunc
from AES import encrypt
import pyperclip as py


def hideFunc(secret_message, cover_message):
    """
    Hide the secret message inside the cover message.
    A new encryption key is created and embedded automatically.
    """

    # Encrypt the secret message using the automatic key system
    encrypted_secret_message = encrypt(secret_message)
    print("Encrypted secret message to be hidden:", encrypted_secret_message)

    # Embed the encrypted secret message inside the cover message
    stego_message = embedFunc(encrypted_secret_message, cover_message)
    print("Steganographic message:", stego_message)

    # Copy the stego message to the clipboard
    py.copy(stego_message)

    return stego_message
