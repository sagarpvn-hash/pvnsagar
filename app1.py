
import streamlit as st

st.title("Student Percentage & Grade Calculator")

num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)

marks = []
if num_subjects:
    st.write("Enter marks for each subject (out of 100):")
    for i in range(int(num_subjects)):
        mark = st.number_input(f"Subject {i+1} marks:", min_value=0, max_value=100, step=1, key=f"mark_{i}")
        marks.append(mark)

    if all(m is not None for m in marks) and len(marks) == num_subjects:
        if st.button("Calculate"):
            total = sum(marks)
            percentage = (total / (num_subjects * 100)) * 100

            if percentage >= 90:
                grade = "A"
            elif percentage >= 80:
                grade = "B"
            elif percentage >= 70:
                grade = "C"
            elif percentage >= 60:
                grade = "D"
            else:
                grade = "F"

            st.success(f"Percentage: {percentage:.2f}%")
            st.success(f"Grade: {grade}")