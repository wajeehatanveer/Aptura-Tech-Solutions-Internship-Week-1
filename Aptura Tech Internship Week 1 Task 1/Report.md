# Student Record System
## Aptura Tech Solution – Python Internship
### Week 1 – Task 1

---

## 1. Project Title

**Student Record System**

---

## 2. Objective

The objective of this project is to develop a simple and user-friendly Student Record System using Python and Streamlit.

The application allows users to manage student information efficiently through an interactive web interface.

---

## 3. Technologies Used

- Python
- Streamlit
- JSON
- Object-Oriented Programming

---

## 4. Project Description

The Student Record System provides functionality for managing student records.

Users can add new students, view existing records, search for a student by ID, update student information, and delete records.

The application uses a JSON file for data persistence, allowing student records to remain available after restarting the application.

---

## 5. Main Features

### Add Student
Users can add a new student by providing:

- Student ID
- Student Name
- Age
- Course
- Marks

The system checks for duplicate Student IDs before adding a new record.

### View Students
All saved student records are displayed in a structured table.

### Search Student
Users can search for a specific student using their Student ID.

### Update Student
Existing student information can be modified, including:

- Name
- Age
- Course
- Marks

### Delete Student
Users can delete an existing student record using the Student ID.

### Dashboard
The application displays useful statistics:

- Total Students
- Average Marks
- Highest Marks

---

## 6. Data Persistence

Student records are stored in a JSON file named:

`students.json`

The application automatically loads existing records when it starts and saves changes whenever records are added, updated, or deleted.

---

## 7. Input Validation

Basic input validation has been implemented to improve reliability.

The system:

- Prevents duplicate Student IDs.
- Requires Student Name.
- Requires Course.
- Restricts Age to a valid range.
- Restricts Marks between 0 and 100.
- Handles cases where a Student ID does not exist.

---

## 8. Project Structure

```text
Aptura Tech Internship Week 1 Task 1/
│
├── app.py
├── studentmanager.py
├── students.json
├── requirements.txt
├── README.md
├── Report.md
└── screenshots/
````

---

## 9. How to Run the Project

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the application using:

```bash
streamlit run app.py
```

The application will open in the web browser.

---

## 10. Testing

The following functionalities were tested:

| Functionality    | Status   |
| ---------------- | -------- |
| Add Student      | ✅ Passed |
| View Students    | ✅ Passed |
| Search Student   | ✅ Passed |
| Update Student   | ✅ Passed |
| Delete Student   | ✅ Passed |
| Data Persistence | ✅ Passed |
| Input Validation | ✅ Passed |

---

## 11. Conclusion

The Student Record System successfully demonstrates the use of Python, Object-Oriented Programming, JSON-based data storage, and Streamlit for building an interactive application.

The project provides essential CRUD operations and a simple dashboard for managing student information efficiently.

---

## 12. Internship Information

**Organization:** Aptura Tech Solution
**Program:** Python Internship
**Week:** 1
**Task1:** Student Record System

````
