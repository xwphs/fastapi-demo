"""
工具函数
"""

import hashlib
import uuid

def random_str():
    only = hashlib.md5(str(uuid.uuid1()).encode()).hexdigest()
    return only