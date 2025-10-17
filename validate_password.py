# Question 1
def validate_password(password: str) -> bool:
    """
    STEP 1: Create a function that validates a password based on the following rules:
        - It must be at least 8 characters long.
        - It must contain at least one uppercase letter.
        - It must contain at least one lowercase letter.
        - It must contain at least one digit.
        - It must contain at least one special character (e.g. @, #, $, %, !).

    TODO: Implement logic to check all these conditions and return True if valid, otherwise False.
    """
    return False


# Question 2
def password_strength(password: str) -> str:
    """
    STEP 2: Determine the strength of a given password and return it as a string.

    Criteria:
        - "Weak" if the password is less than 8 characters long.
        - "Moderate" if it has 8 or more characters but is missing one or more
          of the following: uppercase, lowercase, digit, or special character.
        - "Strong" if it meets all password validation rules from Question 1.

    TODO: Implement the function to return one of these three strings.
    """

    return ""
