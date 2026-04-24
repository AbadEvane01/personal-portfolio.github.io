import streamlit as st
st.title("💼 My Projects")
projects = {
    "Portfolio Website": "📚 It displays my introduction, skills, projects, and contact information in a clean and simple layout.",
    "Data Visualization App": "📊 A simple data visualization project using python. It generates graphs using Matplotlib to help understand patterns in data.",
    "School System": "📨 A basic CRUD (Create, Read, Update, Delete) system for managing school records."
}
for project, desc in projects.items():
    st.subheader(project)
    st.write(desc)