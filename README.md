# 🤖 AI Problem Solving Project

## 📌 Objective
This project demonstrates Artificial Intelligence problem-solving techniques using Python and Streamlit. It includes game AI, constraint satisfaction, and optimization problems.

---

# 🎮 Application 1 — Tic-Tac-Toe AI (Game Playing System)

## 📌 Problem Description
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

## 📌 Output
- Interactive Tic-Tac-Toe board
- Execution time displayed
- Nodes explored displayed

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

## 📌 Output
- Completed Sudoku grid
- Constraint-based solution

---

# 🗺 Application 3 — TSP (Travel Planner System)

## 📌 Problem Description
The Travelling Salesman Problem (TSP) finds the shortest possible route that visits all cities exactly once and returns to the starting city.

It is a classical optimization problem with factorial time complexity.

---

## 🧠 Algorithm Used

### Brute Force Permutation Search
- Fix starting city
- Generate all permutations of remaining cities
- Compute total distance for each route
- Select minimum cost route

---

## ⚙️ Working Logic
Best = ∞  
For each permutation:
- Build full route
- Compute total distance
- Compare with best route
- Store minimum path

---

## 📊 Time Complexity
- O(n!) factorial complexity  
- Suitable for small inputs (≤10 cities)

---

## 🚀 Execution Steps
1. Add cities
2. Enter distances between cities
3. Click "Find Optimal Route"
4. System displays shortest path

---

## 📌 Output
- Optimal route path
- Total distance calculation

---

# 🧠 Technologies Used
- Python
- Streamlit
- Artificial Intelligence Algorithms

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