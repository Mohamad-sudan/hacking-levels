import hashlib

print("=== Level 5 - Secure Vault Builder ===")

def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

my_password = "sudan123"
hashed = make_hash(my_password)

print(f"Your password: {my_password}")
print(f"Secured as hash: {hashed}")

guess = input("Try to guess my password to verify: ")

if make_hash(guess) == hashed:
    print("FLAG: Level5_Crypto_Master_Sudan")
else:
    print("Wrong! Hashes don't match.")
