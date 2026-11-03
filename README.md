# Streamlit To-Do List Application

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A clean, responsive interactive task management application built using Python and Streamlit, featuring dynamic session state persistence, interactive checklist items, task deletion, and a standalone CLI terminal version.

---

## Project Overview

Task management applications provide an excellent foundation for mastering reactive state management and event-driven user interfaces in web development.

This repository features two implementations:
1. **Interactive Web Application (`app.py`)**: A Streamlit single-page application utilizing reactive session state (`st.session_state`) for instant adding, checking off, and deleting of daily items without external database overhead.
2. **Terminal Console Interface (`todo.py`)**: A lightweight command-line interface demonstrating basic loop constructs, input validation, and list manipulations.

### Problem Statement
- **Session Volatility**: Web applications without explicit session management reload state on every button click, resetting entered user tasks.
- **Overengineered Overheads**: Simple to-do utilities often introduce heavy SQL or external server dependencies when lightweight in-memory session persistence is optimal.

---

## Key Features

- **Reactive State Management**: Uses `st.session_state` to retain task lists across re-renders.
- **Dynamic UI Columns**: Side-by-side checkbox rendering with individual deletion actions.
- **Batch Clear**: One-click deletion to reset the active task queue.
- **Dual Interface**: Run either in a web browser (`app.py`) or purely inside a terminal (`todo.py`).

---

## Architecture Flow

```
[ User Interaction ]
         │
         ├── Add Task ─────────► [ Append to st.session_state.tasks ]
         ├── Toggle Complete ──► [ Checkbox State Event ]
         ├── Delete Task ──────► [ Pop index from st.session_state ]
         └── Clear All ────────► [ Reset task list to [] ]
                                           │
                                           ▼
                                 [ st.rerun() Trigger ]
                                           │
                                           ▼
                               [ Updated Reactive View ]
```

---

## Project Structure

```
streamlit-todo-app/
├── app.py              # Streamlit interactive web application
├── todo.py             # Command-line interface version
├── requirements.txt    # Pinned dependency (Streamlit)
├── .gitignore          # Cache and environment exclusions
└── README.md           # Documentation
```

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pratapashanmukhi/streamlit-todo-app.git
   cd streamlit-todo-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows:
   python -m venv venv
   .\venv\Scripts\activate

   # Linux / macOS:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Web Application

```bash
streamlit run app.py
```
*Navigate to `http://localhost:8501`.*

### Running the Terminal CLI Version

```bash
python todo.py
```

---

## Author

**Shanmukhi Pratapa**  
B.Tech Computer Science & Engineering (Artificial Intelligence & Machine Learning)  
VIT-AP University  
GitHub: [@pratapashanmukhi](https://github.com/pratapashanmukhi)
