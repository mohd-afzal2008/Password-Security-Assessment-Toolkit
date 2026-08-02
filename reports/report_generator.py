from datetime import datetime


def generate_report():

    print("=" * 40)
    print("Security Audit Report Generator")
    print("=" * 40)


    username = input("Enter user name: ")

    password = input("Enter analyzed password: ")


    length = len(password)


    score = 0
    issues = []


    if length >= 12:
        score += 2
    else:
        issues.append(
            "Password length should be at least 12 characters"
        )


    if any(c.isupper() for c in password):
        score += 1
    else:
        issues.append(
            "Missing uppercase characters"
        )


    if any(c.islower() for c in password):
        score += 1
    else:
        issues.append(
            "Missing lowercase characters"
        )


    if any(c.isdigit() for c in password):
        score += 1
    else:
        issues.append(
            "Missing numbers"
        )


    if any(not c.isalnum() for c in password):
        score += 1
    else:
        issues.append(
            "Missing special symbols"
        )


    if score <= 2:
        strength = "Weak"

    elif score <= 5:
        strength = "Medium"

    else:
        strength = "Strong"



    report = f"""
====================================
PASSWORD SECURITY AUDIT REPORT
====================================

Generated:
{datetime.now()}

User:
{username}


Password Length:
{length}


Security Score:
{score}/6


Strength:
{strength}


Issues Found:
"""


    if issues:

        for issue in issues:
            report += "\n- " + issue

    else:

        report += "\nNo major issues found."


    report += """



Recommendations:

- Use minimum 12 characters
- Avoid names and birthdays
- Use uppercase, lowercase,
  numbers and symbols
- Enable Multi Factor Authentication


====================================
END OF REPORT
====================================
"""


    with open(
        "output/security_report.txt",
        "w"
    ) as file:

        file.write(report)


    print("\nReport Generated Successfully!")
    print("Saved: output/security_report.txt")