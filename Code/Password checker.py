from Utility import Password, speak

print("Welcome to password strength program\n")

password = input("Enter a password to check strength: ")

st = Password().Strength(password)

print(f"Strength: {st}")
speak(f"Your Password Strength Is {st}")



