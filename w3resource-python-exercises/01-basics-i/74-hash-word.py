import hashlib

def hash_word(word):
    word_bytes = word.encode()
    hash_sha256 = hashlib.sha256(word_bytes).hexdigest()
    print(hash_sha256)

input_word = 'w3r'
hash_word(input_word)
