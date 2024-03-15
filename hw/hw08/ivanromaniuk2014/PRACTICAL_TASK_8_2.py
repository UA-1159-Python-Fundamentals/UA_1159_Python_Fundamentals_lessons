from string import ascii_uppercase, digits, ascii_lowercase

def valid_pasword(psw: str):
    """
    Checks if a string meets the criteria for a valid password.

    Parameters:
    psw (str): The string to be checked for validity as a password.

    Returns:
    bool: True if the string is a valid password; False if the string does not meet the password criteria.

    Password Criteria:
    - Minimum length of 6 characters.
    - Maximum length of 16 characters.
    - Must include digits, uppercase and lowercase letters, and the symbols '$#@'.
    """
    symbols = "$#@"
    max_characters = 16
    min_characters = 6


    if len(psw) >= min_characters and len(psw) < max_characters:
        if any( _ in symbols  for _ in psw) and any ( _ in digits for _ in psw) \
        and any( _ in ascii_uppercase  for _ in psw) and any ( _ in ascii_lowercase for _ in psw):
            return True
        
    return False
                  
                          
