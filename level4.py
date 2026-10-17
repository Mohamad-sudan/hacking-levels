import base64

print("=== Level 4 - Decode the Secret ===")
coded = "RkxBRzogU3VkYW5fSGFja2VyX0xldmVsNF9XaW5uZXI="

print(f"Code found: {coded}")
print("Decoding...")

decoded = base64.b64decode(coded).decode()
print(decoded)
