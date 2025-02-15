import re

def check_password_strength(password):
    strength = 0
    tips = []

    if len(password) >= 8:
        strength += 1
    else:
        tips.append("Make your password at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        tips.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        tips.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        tips.append("Include at least one number.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        tips.append("Include at least one special character (@$!%*?&).")

    if strength == 5:
        return "Strong Password 💪", tips
    elif strength >= 3:
        return "Moderate Password ⚠️", tips
    else:
        return "Weak Password 🚨", tips

# Get user input
password = input("Enter your password: ")
result, suggestions = check_password_strength(password)

print(f"Password Strength: {result}")

if suggestions:
    print("Tips to improve your password:")
    for tip in suggestions:
        print(f"- {tip}")