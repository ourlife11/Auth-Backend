from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import bcrypt
import hashlib

SECRET_KEY = "CHANGE_THIS_TO_ENV_VAR"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # Step 1: Normalize & pre-hash
    sha = hashlib.sha256(password.encode("utf-8")).digest()

    # Step 2: bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(sha, salt)

    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    sha = hashlib.sha256(password.encode("utf-8")).digest()
    return bcrypt.checkpw(sha, hashed_password.encode("utf-8"))


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
