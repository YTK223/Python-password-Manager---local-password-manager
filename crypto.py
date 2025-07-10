def encrypt(text):
    """
    Encrypts a given string using a Caesar cipher-like method.
    
    - Letters are shifted forward by 3 (wraps around the alphabet).
    - Digits are also shifted forward by 3 (wraps around 0-9).
    - All other characters are left unchanged.

    Args:
        text (str): The plaintext string to encrypt.

    Returns:
        str: The encrypted string.
    """
    result = ''
    for char in text:
        if char.isalpha():
            # Shift letter characters forward by 3 positions
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 3) % 26 + base)
        elif char.isdigit():
            # Shift digit characters forward by 3 positions
            result += chr((ord(char) - ord("0") + 3) % 10 + ord("0"))
        else:
            # Leave special characters unchanged
            result += char
    return result


def decrypt(text):
    """
    Decrypts a string that was encrypted using the encrypt() function.

    - Letters are shifted backward by 3 (wraps around the alphabet).
    - Digits are also shifted backward by 3 (wraps around 0-9).
    - All other characters are left unchanged.

    Args:
        text (str): The encrypted string.

    Returns:
        str: The decrypted (original) string.
    """
    result = ''
    for char in text:
        if char.isalpha():
            # Shift letter characters backward by 3 positions
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - 3) % 26 + base)
        elif char.isdigit():
            # Shift digit characters backward by 3 positions
            result += chr((ord(char) - ord("0") - 3) % 10 + ord("0"))
        else:
            # Leave special characters unchanged
            result += char
    return result
