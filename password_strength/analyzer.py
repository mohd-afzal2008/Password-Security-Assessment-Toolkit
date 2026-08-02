import re
import math


COMMON_PASSWORDS = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "password123",
    "12345678",
    "abc123"
]


def calculate_entropy(password):

    charset = 0

    if re.search("[a-z]", password):
        charset += 26

    if re.search("[A-Z]", password):
        charset += 26

    if re.search("[0-9]", password):
        charset += 10

    if re.search("[^a-zA-Z0-9]", password):
        charset += 32


    if charset == 0:
        return 0


    entropy = len(password) * math.log2(charset)

    return round(entropy, 2)



def analyze_password():

    print("=" * 40)
    print("Password Strength Analyzer")
    print("=" * 40)


    password = input("Enter Password : ")


    score = 0
    suggestions = []


    # Length check
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        suggestions.append(
            "Increase password length (minimum 12 characters)"
        )


    # Uppercase
    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append(
            "Add uppercase letters"
        )


    # Lowercase
    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append(
            "Add lowercase letters"
        )


    # Numbers
    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add numbers"
        )


    # Symbols
    if re.search("[^a-zA-Z0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add symbols like @ # $ %"
        )


    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append(
            "Password is commonly used"
        )


    entropy = calculate_entropy(password)


    print("\n========== RESULT ==========")

    print("Length :", len(password))


    print(
        "Uppercase :",
        "Yes" if re.search("[A-Z]", password) else "No"
    )

    print(
        "Lowercase :",
        "Yes" if re.search("[a-z]", password) else "No"
    )

    print(
        "Numbers :",
        "Yes" if re.search("[0-9]", password) else "No"
    )

    print(
        "Symbols :",
        "Yes" if re.search("[^a-zA-Z0-9]", password) else "No"
    )


    print("Entropy :", entropy, "bits")


    if score <= 2:
        strength = "Weak"

    elif score <= 5:
        strength = "Medium"

    else:
        strength = "Strong"


    print("Strength :", strength)


    print("\nRecommendations:")


    if suggestions:

        for item in suggestions:
            print("-", item)

    else:
        print("No improvements needed!")

