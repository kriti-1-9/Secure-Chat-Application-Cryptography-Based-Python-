from key_exchange import generate_keys, generate_shared_key

# User A
priv_a, pub_a = generate_keys()

# User B
priv_b, pub_b = generate_keys()

# Exchange keys
shared_a = generate_shared_key(priv_a, pub_b)
shared_b = generate_shared_key(priv_b, pub_a)

print(shared_a == shared_b)  # Should be True