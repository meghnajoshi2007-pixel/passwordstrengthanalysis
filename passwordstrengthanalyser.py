# Password Strength Analyser

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    if any(char in special for char in password):
        score += 1

    if score == 3:
        return "Strong Password 💪"
    elif score == 2:
        return "Medium Password 🙂"
    else:
        return "Weak Password ⚠️"

print("====== SIMPLE PASSWORD STRENGTH ANALYSER ======")
pwd = input("Enter a password: ")

result = password_strength(pwd)
print(result)
