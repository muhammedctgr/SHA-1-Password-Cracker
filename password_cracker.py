import hashlib


def crack_sha1_hash(hash, use_salts=False):
    """  
    A function that takes in a SHA-1 hash of a password and
    compares it to a list of common passwords.

    The function hashes each password contained in a list of 
    the 10,000 most common passwords, and compares it with
    a hash that is passed into the function.

    Returns the password that is found, or informs the user
    that the password is not in the database

    Parameters
    ----------
    hash : str,
        The SHA1 hash used to compare with hashed passwords\n
    use_salts : boolean, optional,
        Whether or not to append/prepend salt hashes
    """

    try:
        password_found = False

        passwords = open("top-10000-passwords.txt", "r")

        # Loop through each password contained in the list
        for password in passwords:
            # Check for optional argument "use_salts"
            if use_salts == True:
                with open("known-salts.txt", "r") as salts:
                    for salt in salts:
                        # Strip the salt and password of newlines
                        salt = salt.splitlines()[0]
                        password = password.splitlines()[0]

                        # Generate hashes from prepending and appending salt hash
                        prepend_digest = hashlib.sha1(
                            (salt +
                             password).encode("UTF-8").strip()).hexdigest()
                        append_digest = hashlib.sha1(
                            (password +
                             salt).encode("UTF-8").strip()).hexdigest()

                        # If either the prepend_digest or append_digest match the given hash, send password
                        if prepend_digest == hash or append_digest == hash:
                            salts.close()
                            passwords.close()

                            password_found = True

                            return password
            # No use_salts arguements
            else:
                password = password.splitlines()[0]
                enc_password = password.encode("UTF-8")
                digest = hashlib.sha1(enc_password.strip()).hexdigest()

                # Generated digested matches hash
                if digest == hash:
                    passwords.close()
                    password_found = True
                    return password

        # No matches in the database
        if password_found == False:
            passwords.close()
            return "PASSWORD NOT IN DATABASE"

    except FileNotFoundError:
        print("Error: file not found")
        quit()
