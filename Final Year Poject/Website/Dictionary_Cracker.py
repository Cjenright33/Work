import hashlib

def crack_hash(target_hash, dictionary_file):
    with open(dictionary_file, 'r') as f:
        for word in f:
            word = word.strip()
            hash = hashlib.sha256(word.encode()).hexdigest()
            if hash == target_hash:
                return word
    return None

target_hash = input("Enter the hash to crack: ")
dictionary_file = input("Enter the path to the dictionary file: ")
result = crack_hash(target_hash, dictionary_file)
if result:
    print(f"The original message is: {result}")
else:
    print("The hash could not be cracked.")
