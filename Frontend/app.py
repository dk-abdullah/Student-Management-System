import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Student Management System", layout= "wide")

st.title("Student Management System")

menu = st.sidebar.selectbox("Menu",["View Student","Add Student","Search Student","Update Student","Delete Student"])

if menu == "View Student":
    st.subheader("All Students")

    response = requests.get(f"{API_URL}/view")

    if response.status_code == 200:
        students = response.json()
        st.json(students)
    else:
        st.error("Failed to fetch students")


elif menu == "Add Student":
    st.subheader("Add New Student")

    with st.form("add_student"):
        sid = st.text_input("Student ID")
        name = st.text_input("Name")
        age = st.number_input("Age")
        roll = st.text_input("Roll No")
        dept = st.text_input("Department")
        sem = st.text_input("Semester")
        sec = st.text_input("Section")
        badge = st.text_input("Badge")
        gender = st.selectbox("Gender",["male","female"])
        city = st.text_input("City")

        submit = st.form_submit_button("Create Student")

        if submit:
            student_data ={
                "id": sid,
                "Name": name,
                "age": age,
                "roll_no": roll,
                "Department": dept,
                "Semester": sem,
                "Section": sec,
                "Badge": badge,
                "Gender": gender,
                "City": city
            }

            response = requests.post(f"{API_URL}/create", json=student_data)

            if response.status_code== 201:
                st.success("Student Created Successfully")
            else:
                st.error(response.text)

elif menu =="Search Student":
    st.subheader("Search Student")

    student_id = st.text_input("Enter Student ID(e.g s001)")

    if st.button("Search"):
        response = requests.get(f"{API_URL}/Student/{student_id}")

        if response.status_code==200:
            st.success("Student Found")
            st.json(response.json())
        else:
            st.error("Sudent Not Found")

elif menu =="Update Student":
    st.subheader("Update Student")

    sid = st.text_input("Student ID to Update")

    name = st.text_input("New Name(optional)")
    age = st.text_input("New Age(Optional)")
    city = st.text_input("New City(optional)")

    if st.button("Update"):
        update_data = {}

        if name:
            update_data["Name"] = name
        if age:
            update_data["age"] = age
        if city:
            update_data["City"] = city
        
        response = requests.put(f"{API_URL}/edit/{sid}", json=update_data)

        if response.status_code==200:
            st.success("Student Updated ")
        else:
            st.error(response.text)

elif menu == "Delete Student":
    st.subheader("Delete Student")

    sid = st.text_input("Student ID to Delete")

    if st.button("Delete"):
        response = requests.delete(f"{API_URL}/delete/{sid}")

        if response.status_code==200:
            st.success("Student Deleted")
        else:
            st.error(response.text)