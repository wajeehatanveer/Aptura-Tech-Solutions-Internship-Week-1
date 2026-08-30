````markdown
# 🎯 Number Guessing Game

## Aptura Tech Solution – Python Internship

### Week 1 – Task 2

---

## 1. Project Title

**Number Guessing Game**

---

## 2. Objective

The objective of this project is to develop an interactive Number Guessing Game using Python and Streamlit.

The game challenges the user to guess a randomly generated number between 1 and 100 while providing hints after each attempt.

---

## 3. Technologies Used

- Python
- Streamlit
- Random Module
- Object-Oriented Programming

---

## 4. Project Description

The Number Guessing Game generates a random secret number between 1 and 100.

The user enters a guess through the Streamlit interface. The application provides feedback based on the guess:

- ⬆️ Too Low
- ⬇️ Too High
- 🎉 Correct

The game also keeps track of the number of attempts and allows the user to start a new game after successfully guessing the number.

---

## 5. Main Features

- 🎲 Random number generation
- 🔢 Number range from 1 to 100
- 🎯 User guessing system
- ⬆️ Too Low feedback
- ⬇️ Too High feedback
- 🎉 Correct guess notification
- 📊 Attempts counter
- 🔄 New Game option
- 🎨 Interactive Streamlit interface

---

## 6. Game Logic

The game uses Python's `random` module to generate a secret number.

The user's guess is compared with the secret number.

If the guess is:

- Lower than the secret number → **Too Low**
- Higher than the secret number → **Too High**
- Equal to the secret number → **Correct**

The number of attempts is increased after every valid guess.

---

## 7. Project Structure

```text
Aptura Tech Internship Week 1 Task 2/
│
├── app.py
├── game.py
├── requirements.txt
├── README.md
├── Report.md
└── screenshots/
````

---

## 8. Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## 9. How to Run

Run the following command in the terminal:

```bash
streamlit run app.py
```

The game will open in the web browser.

---

## 10. How to Play

1. Start the application.
2. Enter a number between 1 and 100.
3. Click **Submit Guess**.
4. Follow the hint provided by the application.
5. Continue guessing until the correct number is found.
6. Click **Start New Game** to play again.

---

## 11. Screenshots

Screenshots demonstrating the game interface and functionality are available in the `screenshots` folder.

---

## 12. Conclusion

The Number Guessing Game successfully demonstrates the use of Python, Object-Oriented Programming, random number generation, and Streamlit to create an interactive application.

The project provides a simple and engaging user experience while following a clean separation between game logic and the user interface.

---

## 13. Internship Information

**Organization:** Aptura Tech Solution
**Program:** Python Internship
**Batch:** Batch 3
**Week:** Week 1
**Task:** Task 2 – Number Guessing Game

```
