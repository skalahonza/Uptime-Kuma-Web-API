from passlib.context import CryptContext

# Create a single instance of CryptContext for better performance and thread safety.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash the given password.

    :param password: The password to hash
    :return: The hashed password as a string
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify if the given password matches the hashed password.

    :param password: The password to verify
    :param hashed_password: The hashed password to compare with
    :return: True if the password matches, False otherwise
    """
    return pwd_context.verify(password, hashed_password)
