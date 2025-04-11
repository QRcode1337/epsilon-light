import nacl.signing
import hashlib

def generate_identity():
    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    node_id = hashlib.sha256(verify_key.encode()).hexdigest()
    return node_id, signing_key, verify_key
