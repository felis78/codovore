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
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

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

def connect_mariadb():
    try:
        database_connection = mariadb.connect(
            user="codovore",
            password="z4526A",
            host="127.0.0.1",
            port=3306,
            database="codovore"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

        # Get Cursor
    return database_connection

def create_users(connection, username, hashed_password, email, level):
    try:
        cursor = connection.cursor()
        sql="INSERT INTO users (name, email, level, password) VALUES (%s, %s, %s , %s)"
        datas=(username, email, level, hashed_password)
        cursor.execute(sql, datas)
        connection.commit()
        
    except mariadb.Error as e:
        print(f"Error push user to MariaDB Platform: {e}")
        cursor.close
        return(False)
    
    cursor.close
    return True

    
    
def get_all_user(connection):
    users=[]
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, email, level, password FROM users")
    for (id, name, email, level, password) in cursor:
        users.append(f"{id}, {name}, {email}, {level}, {password}")
    
    if len(users) != 0:
        cursor.close()
        return users
        
    cursor.close()
    return False
        
    
    
def verify_user(connection, email, password_to_test):
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM users WHERE email = %s", [email])
    for (password) in cursor:
        if verify_password(password_to_test, password[0]):
            cursor.close()
            return True
        cursor.close()
        return False
    
# def deluser(connection, email):
#     try:
#         cursor = connection.cursor()
#         cursor.execute("DELETE FROM users WHERE email=%s", (email,))
#         cursor.commit()
#         cursor.close()
#         return True
    
#     except mariadb.Error as e:
#         print(f"Error delete user from MariaDB Platform: {e}")
#         cursor.close()
#         return False
    

    
