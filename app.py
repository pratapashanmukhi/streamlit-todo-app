import streamlit as st

st.title("To Do List App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)

st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4,1])
    
    col1.write(t)
    
    if col2.button("Delete", key=i):
        st.session_state.tasks.pop(i)
        st.rerun()