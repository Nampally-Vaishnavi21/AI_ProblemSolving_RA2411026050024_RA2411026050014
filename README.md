#  AI Problem Solving Project

##  Objective
This project demonstrates Artificial Intelligence problem-solving techniques using Python and Streamlit. It includes game AI, constraint satisfaction, and optimization problems.

---

#  Application 1 — Tic-Tac-Toe AI (Game Playing System)

##  Problem Description
Tic-Tac-Toe is a two-player game where the goal is to get three marks in a row. In this project, an AI opponent is implemented that plays optimally against the user.

The AI ensures it never loses by analyzing all possible future moves.

---

## 🧠 Algorithms Used

### 1. Minimax Algorithm
- Explores all possible game states
- Assumes both players play optimally
- Chooses the best possible move for AI

### 2. Alpha-Beta Pruning
- Optimized version of Minimax
- Eliminates unnecessary branches
- Reduces computation time and number of nodes explored

---

## ⚙️ Working Logic
- AI evaluates all possible moves
- Assigns scores:
  - Win → +1  
  - Loss → -1  
  - Draw → 0  
- Selects move with maximum score

---

## 📊 Comparison
- Minimax explores more nodes
- Alpha-Beta Pruning is faster and more efficient

---

## 🚀 Execution Steps
1. Start the application
2. Choose algorithm (Minimax / Alpha-Beta)
3. Click on the grid to make a move
4. AI responds automatically

---

### 📊 Sample Output

User Move: X at position 1  
AI Move: O at position 5  

Board:
X |   |  
---------
  | O |  
---------
  |   |  

Result: Draw  

Execution Time: 0.00021 sec  
Nodes Explored: 549

---

# 🧩 Application 2 — Sudoku Solver (CSP Problem)

## 📌 Problem Description
Sudoku is a Constraint Satisfaction Problem (CSP) where a 9×9 grid must be filled so that each row, column, and 3×3 subgrid contains digits 1–9 without repetition.

---

## 🧠 Algorithm Used

### Backtracking (CSP)
- Try filling empty cells recursively
- Check constraints at each step
- Backtrack if constraints fail

---

## ⚙️ Working Logic
1. Find an empty cell
2. Try numbers 1–9
3. Check validity (row, column, subgrid)
4. Recursively continue
5. Backtrack if needed

---

## 🚀 Execution Steps
1. Enter Sudoku grid (use 0 for empty cells)
2. Click "Solve Sudoku"
3. AI solves the puzzle instantly

---

### 📊 Sample Output

Input:
0 0 3 0 2 0 6 0 0  
9 0 0 3 0 5 0 0 1  
0 0 1 8 0 6 4 0 0  

Output:
4 8 3 9 2 1 6 5 7  
9 6 7 3 4 5 8 2 1  
2 5 1 8 7 6 4 9 3  

---


# 📁 Project Structure
AI_ProblemSolving_Project/
│
├── app.py
├── README.md
├── requirements.txt
│
├── TicTacToe/
│ └── tictactoe.py
│
├── Sudoku/
│ └── sudoku_solver.py
│
└── TSP/
└── tsp.py (if implemented)

---

# 🚀 How to Run
pip install streamlit
streamlit run app.py

---

# 🎯 Final Outcome
This project demonstrates:
- Game AI (Tic-Tac-Toe)
- Constraint Satisfaction (Sudoku)
- Optimization Problem (TSP)

---

# 📌 Key Highlights
- AI-based decision making
- Optimization algorithms
- Constraint solving techniques
- Interactive Streamlit UI
