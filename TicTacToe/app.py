import streamlit as st
from TicTacToe.tictactoe import *

st.title("Tic-Tac-Toe AI")

if "board" not in st.session_state:
    st.session_state.board = [" "] * 9

method = st.selectbox("Choose Algorithm", ["Minimax", "Alpha-Beta"])

cols = st.columns(3)

for i in range(9):
    if cols[i % 3].button(st.session_state.board[i], key=i):
        if st.session_state.board[i] == " ":
            st.session_state.board[i] = "X"

            move, t, nodes = get_best_move(st.session_state.board, method)

            if move != -1:
                st.session_state.board[move] = "O"

            st.write(f"Execution Time: {t:.5f} sec")
            st.write(f"Nodes Explored: {nodes}")

winner = check_winner(st.session_state.board)

if winner:
    st.success(f"Winner: {winner}")
