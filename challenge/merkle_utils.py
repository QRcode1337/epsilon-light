import hashlib

def merkle_hash(data_list):
    if len(data_list) == 1:
        return hashlib.sha256(data_list[0].encode()).hexdigest()
    mid = len(data_list) // 2
    left = merkle_hash(data_list[:mid])
    right = merkle_hash(data_list[mid:])
    return hashlib.sha256((left + right).encode()).hexdigest()
