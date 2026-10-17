# Top Secret System - Level 2
secret = "sudan123"
print("=== Welcome to Secret Vault ===")
print("Guess the password to hack it!")

for i in range(3):
    guess = input("Enter password: ")
    if guess == secret:
        print("ACCESS GRANTED! You hacked it!")
        print("FLAG: Mohmad_Is_A_Hacker_2026")
        break
    else:
        print(f"Wrong! {2-i} tries left")
else:
    print("SYSTEM LOCKED! You failed")

# Hint for real hackers: password is inside this file
