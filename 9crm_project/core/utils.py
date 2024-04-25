"""
工具函数
"""

import hashlib
import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from typing import Union

def random_str():
    only = hashlib.md5(str(uuid.uuid1()).encode()).hexdigest()
    return only

def en_password(pwd):
    return pbkdf2_sha256.hash(pwd)

def check_password(secret: Union[str, bytes], hash: Union[str, bytes]):
    return pbkdf2_sha256.verify(secret, hash)