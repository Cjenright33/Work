import hashlib

def is_hash(input_data):
    hash_types = [
        ('md5', hashlib.md5()),
        ('sha1', hashlib.sha1()),
        ('sha224', hashlib.sha224()),
        ('sha256', hashlib.sha256()),
        ('sha384', hashlib.sha384()),
        ('sha512', hashlib.sha512())
    ]
    for name, hasher in hash_types:
        length = len(hasher.hexdigest())
        if len(input_data) == length:
            try:
                int(input_data, 16)
                return name
            except ValueError:
                pass
    return None

input_data = input("Enter the string to check if it's a hash value: ")
output = is_hash(input_data)
if result:
    print(f"The string is a {output} hash value.")
else:
    print("The string is not a hash value.")
