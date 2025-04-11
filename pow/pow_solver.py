import hashlib
import time

def solve_pow(challenge, difficulty=4):
    prefix = '0' * difficulty
    nonce = 0
    while True:
        text = f"{challenge}{nonce}"
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        if hash_result.startswith(prefix):
            return nonce, hash_result
        nonce += 1
