# Text Steganography

This project is an implementation and GUI enhancement of the **AITSteg** system, based on the original research paper:
**[AITSteg: An Innovative Text Steganography Technique for Hidden Transmission of Text Message via Social Media](https://ieeexplore.ieee.org/document/8440030)**

This implementation hides encrypted messages within plain text using invisible zero-width Unicode characters, combining the AITSteg algorithm for embedding with AES-256 encryption for security.

Text steganography conceals secret messages by embedding them as invisible zero-width characters (ZWC) within a cover message. This implementation uses a combination of cryptographic security and steganographic techniques to ensure both confidentiality and covertness.

## Core Features

**Encryption Layer:**
- **AES-256 Encryption**: Military-grade encryption for secret messages
- **Random Key Generation**: SHA-256 based cryptographically secure key generation
- **Initialization Vector (IV)**: 16-byte random IV for each encryption
- **Key Embedding**: Encryption key bundled with ciphertext for passwordless decryption

**Steganographic Layer:**
- **AITSteg Algorithm**: Advanced Information-Theoretic Steganography
- **Zero-Width Characters (4)**: U+200C, U+202C, U+202D, U+200E
- **Binary Encoding**: 12-bit encoding per character (6-bit alpha + 6-bit beta)
- **XOR Hashing**: Message-secret key hashing for additional obfuscation

**User Interface Features:**
- **File Save/Load**: Download and upload steganographic messages as `.txt` files to preserve invisible characters
- **Clipboard Integration**: Automatic copying of steganographic messages
- **Dual-Panel Interface**: Separate HIDE and REVEAL sections for intuitive workflow

## Setup & Installation

### Prerequisites
Make sure Python 3.x is installed. You can download it from [python.org](https://python.org)

### Clone the Repository
```bash
git clone https://github.com/oag18/Text-steganography-Group.git
cd Text-steganography-Group
```

### Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
**Windows:**
```bash
python app.py
```

**Linux/Mac:**
```bash
python3 app.py
```

### Access the Application
Open your browser and navigate to: **http://localhost:5000**

## Application Functionality

### HIDE Section
- Enter a **secret message** to conceal
- Enter a **cover message** to hide the secret within
- Click **"Hide"** to generate the steganographic message
- **Save to File** button downloads the message as a `.txt` file
- Message automatically copied to clipboard

### REVEAL Section
- Paste the **steganographic message** received
- Or **Load from File** to upload a saved `.txt` file
- Click **"Get Secret"** to decrypt and extract the hidden message
- View the decrypted secret message

## Known Limitations / Security Considerations

**Security:**
- **Passwordless Design**: The AES encryption key is embedded within the steganographic message itself. Anyone who intercepts the message and has access to the code can decrypt it.
- **Public Repository**: Since the algorithm is open-source on GitHub, security relies on the steganographic concealment rather than cryptographic key secrecy.


**Technical:**
- Zero-width characters may be stripped by some text editors or platforms when copy-pasting
- File save/load feature recommended for reliable transfer
- Cover message embedding uses a simple insertion pattern (all ZWCs inserted before the last character)

**Future Work:**
- Distribute zero-width characters more evenly throughout cover message for better steganographic security
- Add support for longer messages and compression
- Implement detection-resistance metrics

## Contributors

Omar, Daniel, John, Bohdan<br>
Texas State University / Cryptography CS.4379H Fall 2025

---


*Based on the original text steganography system by Sakshi Shelar, Nishi Shah, and Sakshi Pandey*

