from extract import extractFunc
from AES import decrypt


def revealFunc(stego_message):
    """
    Reveal and decrypt the secret message found inside the steganographic text.
    The encryption key is extracted from the message automatically.
    """

    # Extract the encrypted secret message from the stego text
    extracted_encrypted_message = extractFunc(stego_message)

    # Decrypt the extracted message using the embedded key
    revealed_secret = decrypt(extracted_encrypted_message)

    print("Revealed secret message:", revealed_secret)
    return revealed_secret
