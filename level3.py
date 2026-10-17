print("=== Level 3 - Auto Guesser ===")
passwords = ["1234", "admin", "mohmad", "sudan123", "khartoum"]

secret = "sudan123"

for p in passwords:
    print(f"Trying: {p}")
    if p == secret:
        print(f"SUCCESS! Found it: {p}")
        break
