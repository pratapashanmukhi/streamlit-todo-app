import streamlit as st

st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="centered")

st.title("📝 Modern To-Do List App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.container():
    col_input, col_add = st.columns([4, 1])
    task = col_input.text_input("Enter a new task", placeholder="What do you need to accomplish today?", label_visibility="collapsed")
    if col_add.button("Add Task", use_container_width=True):
        if task.strip():
            st.session_state.tasks.append(task.strip())
            st.rerun()

st.divider()

col_header, col_clear = st.columns([3, 1])
col_header.subheader(f"Active Tasks ({len(st.session_state.tasks)})")
if st.session_state.tasks and col_clear.button("Clear All", use_container_width=True):
    st.session_state.tasks = []
    st.rerun()

if not st.session_state.tasks:
    st.info("No tasks yet! Add a task above to get started.")
else:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([5, 1])
        col1.checkbox(t, key=f"task_{i}")
        if col2.button("Delete", key=f"delete_{i}", use_container_width=True):
            st.session_state.tasks.pop(i)
            st.rerun()
