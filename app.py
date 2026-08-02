import streamlit as st
import hashlib
import math
import re
import itertools
import string
import time
from datetime import datetime

st.set_page_config(
    page_title="Password Security Assessment Toolkit",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Password Security Assessment Toolkit")
st.markdown("### Educational Cybersecurity Project")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Dictionary Generator",
        "Password Strength Analyzer",
        "Hash Generator",
        "Hash Identifier",
        "Brute-force Simulator",
        "Report Generator"
    ]
)

# ---------------- HOME ---------------- #

if menu == "Home":

    st.header("Welcome")

    st.write("""
This toolkit demonstrates password security concepts in an educational environment.

Modules Included:

- Dictionary Generator
- Password Strength Analyzer
- Hash Generator
- Hash Identifier
- Brute-force Simulator
- Report Generator
""")

# ---------------- DICTIONARY ---------------- #

elif menu == "Dictionary Generator":

    st.header("Dictionary Generator")

    name = st.text_input("Name")

    dob = st.text_input("DOB (DDMMYYYY)")

    if st.button("Generate Dictionary"):

        passwords = set()

        if name:

            passwords.update([
                name.lower(),
                name.upper(),
                name.capitalize(),
                name + "123",
                name + "@123",
                name + "786",
                name + "2026",
                name + dob,
                name + dob[-4:] if len(dob) >= 4 else name
            ])

        st.success("Dictionary Generated")

        st.code("\n".join(sorted(passwords)))

# ---------------- PASSWORD ---------------- #

elif menu == "Password Strength Analyzer":

    st.header("Password Strength Analyzer")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Analyze"):

        score = 0

        suggestions = []

        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            suggestions.append("Increase password length")

        if re.search("[A-Z]", password):
            score += 1
        else:
            suggestions.append("Add uppercase letters")

        if re.search("[a-z]", password):
            score += 1
        else:
            suggestions.append("Add lowercase letters")

        if re.search("[0-9]", password):
            score += 1
        else:
            suggestions.append("Add numbers")

        if re.search("[^a-zA-Z0-9]", password):
            score += 1
        else:
            suggestions.append("Add symbols")

        charset = 0

        if re.search("[a-z]", password):
            charset += 26

        if re.search("[A-Z]", password):
            charset += 26

        if re.search("[0-9]", password):
            charset += 10

        if re.search("[^a-zA-Z0-9]", password):
            charset += 32

        entropy = round(len(password) * math.log2(charset), 2) if charset else 0

        if score <= 2:
            strength = "Weak"
            st.error(strength)
        elif score <= 5:
            strength = "Medium"
            st.warning(strength)
        else:
            strength = "Strong"
            st.success(strength)

        st.write("Entropy:", entropy, "bits")

        if suggestions:
            st.subheader("Suggestions")
            for s in suggestions:
                st.write("•", s)

# ---------------- HASH ---------------- #

elif menu == "Hash Generator":

    st.header("Hash Generator")

    text = st.text_input("Text")

    if st.button("Generate Hashes"):

        st.code(hashlib.md5(text.encode()).hexdigest(), language="text")

        st.code(hashlib.sha256(text.encode()).hexdigest(), language="text")

        st.code(hashlib.sha512(text.encode()).hexdigest(), language="text")

# ---------------- HASH IDENTIFIER ---------------- #

elif menu == "Hash Identifier":

    st.header("Hash Identifier")

    h = st.text_input("Paste Hash")

    if st.button("Identify"):

        if len(h) == 32:
            st.success("MD5")

        elif len(h) == 64:
            st.success("SHA-256")

        elif len(h) == 128:
            st.success("SHA-512")

        else:
            st.error("Unknown Hash")

# ---------------- BRUTE FORCE ---------------- #

elif menu == "Brute-force Simulator":

    st.header("Brute-force Simulator")

    target = st.text_input("Demo Password (max 4 chars)")

    if st.button("Run Simulation"):

        chars = string.ascii_lowercase + string.digits

        attempts = 0

        start = time.time()

        found = False

        for length in range(1, 5):

            for combo in itertools.product(chars, repeat=length):

                attempts += 1

                guess = "".join(combo)

                if guess == target:

                    found = True

                    end = time.time()

                    break

            if found:
                break

        if found:

            st.success("Password Found")

            st.write("Attempts:", attempts)

            st.write("Time:", round(end-start,4), "seconds")

        else:

            st.error("Not Found (try shorter password)")

# ---------------- REPORT ---------------- #

elif menu == "Report Generator":

    st.header("Security Report")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Generate"):

        score = 0

        if len(password) >= 12:
            score += 2

        if any(c.isupper() for c in password):
            score += 1

        if any(c.islower() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(not c.isalnum() for c in password):
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score <= 5:
            strength = "Medium"
        else:
            strength = "Strong"

        report = f"""
PASSWORD SECURITY REPORT

Date: {datetime.now()}

User: {username}

Password Length: {len(password)}

Score: {score}/6

Strength: {strength}

Recommendations:

- Use at least 12 characters
- Include uppercase, lowercase, numbers and symbols
- Avoid common passwords
"""

        st.download_button(
            "Download Report",
            report,
            file_name="security_report.txt"
        )
