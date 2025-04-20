import streamlit as st

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

strength = 0


if len(password) >= 8:
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(not c.isalnum() for c in password):
    strength += 1


st.subheader("Password Strength:")
st.write("★" * strength + "☆" * (4 - strength))


if strength == 4:
    st.success("Strong Password! ✅")
elif strength >= 2:
    st.warning("Medium Strength! ⚠️")
else:
    st.error("Weak Password! ❌")
