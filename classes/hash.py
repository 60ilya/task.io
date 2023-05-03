import hashlib

class Hash:
    def hash_password(password: str):
        hash_object = hashlib.md5(password)

        return hash_object.hexdigest()
    

    