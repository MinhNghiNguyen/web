import streamlit as st
st.set_page_config(layout="wide")
skibidi1, skibidi2 = st.columns([2, 3])

with skibidi1:
    st.button("skibidi")
    st.title("Fake Facebook Login Page")

    email = st.text_input("Email or Phone")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if email == "example@example.com" and password == "password":
            st.success("Login successful")
        else:
            st.error("Login failed. Please check your credentials.")
with skibidi2:
    st.title("Fake Facebook Login Page")
    if st.button("Log In"):
        if email == "example@example.com" and password == "password":
            st.success("Login successful")
        else:
            st.error("Login failed. Please check your credentials.")