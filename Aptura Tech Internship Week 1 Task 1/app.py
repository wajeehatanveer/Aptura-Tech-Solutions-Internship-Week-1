import streamlit as st
from studentmanager import StudentManager


# Page Configuration

st.set_page_config(
    page_title="Student Record System",
    page_icon="🎓",
    layout="wide"
)


# Custom CSS

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        margin-bottom: 25px;
    }

    .card-title {
        font-size: 16px;
        font-weight: 600;
    }

    .card-value {
        font-size: 28px;
        font-weight: 700;
    }

    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# Initialize Student Manager

if "student_manager" not in st.session_state:
    st.session_state.student_manager = StudentManager()

manager = st.session_state.student_manager

# Show success message after rerun
if "success_message" in st.session_state:
    st.success(st.session_state.success_message)
    del st.session_state.success_message


# Header

st.markdown(
    '<div class="main-title">🎓 Student Record System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Manage student records efficiently using Python & Streamlit.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# Dashboard

students = manager.get_all_students()

total_students = len(students)

if students:
    average_marks = sum(
        student["marks"] for student in students
    ) / total_students

    highest_marks = max(
        student["marks"] for student in students
    )
else:
    average_marks = 0
    highest_marks = 0


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👨‍🎓 Total Students", total_students)

with col2:
    st.metric("📊 Average Marks", f"{average_marks:.1f}")

with col3:
    st.metric("🏆 Highest Marks", f"{highest_marks:.1f}")


st.divider()


# Sidebar

st.sidebar.title("🎓 Student Manager")
st.sidebar.caption("Student Record System")

option = st.sidebar.radio(
    "Select an option:",
    [
        "Add Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student"
    ]
)



# Add Student

if option == "Add Student":

    st.header("➕ Add Student")

    with st.form("add_student_form"):

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        name = st.text_input("Student Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            step=1
        )

        course = st.text_input("Course")

        marks = st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            step=0.1
        )

        submitted = st.form_submit_button("➕ Add Student")

        if submitted:

            if not name.strip() or not course.strip():

                st.error(
                    "Please enter the student name and course."
                )

            elif manager.search_student(student_id):

                st.warning(
                    "A student with this ID already exists."
                )

            else:

                student = {
                    "id": student_id,
                    "name": name.strip(),
                    "age": age,
                    "course": course.strip(),
                    "marks": marks
                }

                manager.add_student(student)
                
                st.success(
                    f"Student '{name}' has been added successfully! 🎉"
                )
                
    
# View Students

elif option == "View Students":

    st.header("📋 All Students")

    students = manager.get_all_students()

    if students:

        st.dataframe(
            students,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No student records found.")


# Search Student

elif option == "Search Student":

    st.header("🔍 Search Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    if st.button("🔍 Search"):

        student = manager.search_student(student_id)

        if student:

            st.success("Student found! ✅")

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**Student ID:** {student['id']}")
                st.write(f"**Name:** {student['name']}")
                st.write(f"**Age:** {student['age']}")

            with col2:

                st.write(f"**Course:** {student['course']}")
                st.write(f"**Marks:** {student['marks']}")

        else:

            st.error(
                "No student found with this ID."
            )


# Update Student

elif option == "Update Student":

    st.header("✏️ Update Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    student = manager.search_student(student_id)

    if student:

        st.info(
            f"Updating record for: {student['name']}"
        )

        with st.form("update_student_form"):

            name = st.text_input(
                "Student Name",
                value=student["name"]
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=int(student["age"])
            )

            course = st.text_input(
                "Course",
                value=student["course"]
            )

            marks = st.number_input(
                "Marks",
                min_value=0.0,
                max_value=100.0,
                value=float(student["marks"])
            )

            update_button = st.form_submit_button(
                "✏️ Update Student"
            )

            if update_button:

                if not name.strip() or not course.strip():

                    st.error(
                        "Please enter the student name and course."
                    )

                else:

                    updated_data = {
                        "name": name.strip(),
                        "age": age,
                        "course": course.strip(),
                        "marks": marks
                    }

                    manager.update_student(
                        student_id,
                        updated_data
                    )

                    # st.session_state.success_message = (
                    # "Student record updated successfully! ✅"
                    # )
                    st.success("Student record updated successfully! ✅")
                    
    else:
        st.warning("No student found with this ID.")
                    
                                  
# Delete Student

elif option == "Delete Student":

    st.header("🗑️ Delete Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    student = manager.search_student(student_id)

    if student:

        st.warning(
            f"You are about to delete the record of "
            f"**{student['name']}**."
        )

        if st.button("🗑️ Delete Student"):

            deleted = manager.delete_student(student_id)
            
            
            if deleted:
                st.success("Student record deleted successfully! ✅")
            else:
                st.error("Unable to delete the student record.")

    else:
        st.info("No student found with this ID.")
