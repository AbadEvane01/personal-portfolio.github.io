import streamlit as st
st.title("📩 Contact Me")
st.write("I'd love to connect with you! Whether you have a question, feedback, or a project idea, feel free to reach me out. I'm always open to learning and collaboration.")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Send"):
    if name and email and message:
        st.success(f"Thank you {name}, your message has been received!")
    else:
        st.error("Please fill all fields.")