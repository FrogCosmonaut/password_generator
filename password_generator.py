import random
import string

def generate_password(length=12, complexity="all", pronounceable=False):
    """
    Return a secure and random password.

    Args:
        length (int): Length of the password (default: 12).
        complexity (str): Password complexity. Options: 'all', 'alpha', 'numeric', 'special' (default: 'all').
        pronounceable (bool): Whether to generate a pronounceable password (default: False).

    Returns:
        str: Password.
    """
    complexity = complexity.lower()
    
    if complexity == "all":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "alpha":
        characters = string.ascii_letters
    elif complexity == "numeric":
        characters = string.digits
    elif complexity == "special":
        characters = string.punctuation
    else:
        raise ValueError("Invalid complexity")

    if pronounceable:
        vowels = "aeiou"
        consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
        password = ''.join(random.choice(consonants) + random.choice(vowels) for _ in range(length // 2))
    else:
        password = ''.join(random.choice(characters) for _ in range(length))

    return password
