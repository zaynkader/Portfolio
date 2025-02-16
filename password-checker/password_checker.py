import streamlit as st
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
        return "Strong Password 💪", "green", tips
    elif strength >= 3:
        return "Moderate Password ⚠️", "orange", tips
    else:
        return "Weak Password 🚨", "red", tips

# Streamlit UI
def main():
    st.title("🔒 Password Strength Checker")
    st.write("Enter a password to check its strength and get improvement tips.")
    
    password = st.text_input("Enter your password", type="password")
    if st.button("Check Password"):
        if password:
            result, color, suggestions = check_password_strength(password)
            st.markdown(f"**Password Strength:** <span style='color:{color}; font-weight:bold;'>{result}</span>", unsafe_allow_html=True)
            
            if suggestions:
                st.write("### Suggestions to Improve Your Password:")
                for tip in suggestions:
                    st.write(f"- {tip}")
        else:
            st.warning("Please enter a password to check.")

if __name__ == "__main__":
    main()
