import base64
import hashlib

print("=== FINAL LEVEL 6 - The Hacker Challenge ===")
score = 0

# Stage 1 - Guessing
print("\n[Stage 1] What was the password from Level 2?")
s1 = input("> ")
if s1 == "sudan123":
    print("Correct!")
    score += 1
else:
    print("Wrong, but continue...")

# Stage 2 - Decoding
print("\n[Stage 2] Decode this: U3VkYW4=")
print("What is the hidden word?")
s2 = input("> ")
if s2.lower() == "sudan":
    print("Correct! You know Base64!")
    score += 1
else:
    print(f"Hint: it was {base64.b64decode('U3VkYW4=').decode()}")

# Stage 3 - Hash check
print("\n[Stage 3] Final verification - type 'I_AM_A_HACKER' to win")
s3 = input("> ")
if s3 == "I_AM_A_HACKER":
    score += 1

print(f"\nYour Score: {score}/3")
if score >= 2:
    print("FLAG: FINAL_BOSS_Sudan_Hacker_2026 - YOU WIN!")
    print("You are now a Level 6 Hacker from Omdurman!")
else:
    print("Try again! You need 2 points")
