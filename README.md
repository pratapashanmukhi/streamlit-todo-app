# Streamlit Task Management Application

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A clean, interactive productivity and task management web application built with Streamlit, demonstrating stateful session management, real-time reactive UI updates, and lightweight client-side task persistence.

---

## Features

- **Task Creation & Scheduling**: Add discrete action items with instant state reflection.
- **Completion Tracking**: Interactive checkbox triggers to mark tasks as accomplished.
- **Task Deletion**: Immediate removal of stale tasks with cache invalidation.
- **Session State Persistence**: Uses `st.session_state` to prevent state loss during reactive component rerenders.

---

## Project Structure

```
streamlit-todo-app/
├── app.py              # Main Streamlit web application & interface
├── todo.py             # Underlying task list controller & helper methods
├── requirements.txt    # Dependency manifest
├── .gitignore          # Cache & environment exclusions
└── README.md           # Documentation
```

---

## Installation & Running

```bash
git clone https://github.com/pratapashanmukhi/streamlit-todo-app.git
cd streamlit-todo-app
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

---

## Author

**Shanmukhi Pratapa**  
B.Tech CSE (AI & ML) — VIT-AP University  
GitHub: [@pratapashanmukhi](https://github.com/pratapashanmukhi)
