import hashlib
import mariadb
import sys

def hash_password(password):
    """
    This function takes a password as input and returns its SHA256 hash.

    Parameters:
    password (str): The password to be hashed.

    Returns:
    str: The SHA256 hash of the password.

    Example:
    >>> hash_password('my_password')
    'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    """
    return hash.sha256(password.encode('utf-8')).hexdigest()

def verify_password(password, hashed_password):
    """
    This function verifies if a given password matches the hashed password.

    Parameters:
    password (str): The password to be verified.
    hashed_password (str): The hashed password to be compared.

    Returns:
    bool: True if the password matches the hashed password, False otherwise.

    Note:
    This function calls the hash_password function internally to hash the given password.
    It does not store or return the hashed password.

    Example:
    >>> verify_password('my_password', 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e')
    True
    >>> verify_password('wrong_password', 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e')
    False
    """
    hash_password(password)
    return hashed_password == hash_password(password)


def record_user(username="user", hashed_password='truc', email='email', level="tagueule"):
    try:
        conn = mariadb.connect(
            user="codovore",
            password="z4526A",
            host="192.0.2.1",
            port=3307,
            database="codovore"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()


record_user()
