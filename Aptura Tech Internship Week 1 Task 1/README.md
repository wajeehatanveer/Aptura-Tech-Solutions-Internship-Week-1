# Python Internship — Week 1
# Task 1: 🎓 Student Record System

A Python-based Student Record System built with **Streamlit**.  
The application provides a simple and user-friendly interface to manage student records efficiently.

## 📌 Project Overview

The Student Record System allows users to add, view, search, update, and delete student records through an interactive Streamlit web interface.

Student records are stored in a JSON file so that the data remains available even after restarting the application.

## ✨ Features

- ➕ Add new student records
- 📋 View all student records
- 🔍 Search students by ID
- ✏️ Update existing student information
- 🗑️ Delete student records
- 📊 Dashboard with student statistics
- 💾 JSON-based data persistence
- ✅ Input validation
- ⚠️ Error and status messages
- 🎨 User-friendly Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- JSON
- Object-Oriented Programming

## 📂 Project Structure

```text
Aptura Tech Internship Week 1 Task 1/
│
├── app.py
├── studentmanager.py
├── students.json
├── requirements.txt
├── README.md
└── screenshots/
````

## ⚙️ Installation

Clone or download the project and open the Task 1 folder.

Install the required dependency:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the following command in the terminal:

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🧑‍💻 How to Use

### Add Student

Enter the student's ID, name, age, course, and marks, then click **Add Student**.

### View Students

Select **View Students** from the sidebar to display all saved student records.

### Search Student

Enter a Student ID and click **Search** to find a specific student.

### Update Student

Enter an existing Student ID, modify the required information, and click **Update Student**.

### Delete Student

Enter an existing Student ID and click **Delete Student** to remove the record.

## 💾 Data Storage

Student records are stored in `students.json`.

The application automatically loads existing records when it starts and saves changes whenever a student is added, updated, or deleted.

## 📸 Screenshots

Screenshots demonstrating the application's functionality are available in the `screenshots` folder.

## 🎯 Internship Task

**Aptura TEch Solutions Internship — Week 1**
**Task 1: Student Record System**

