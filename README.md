
# ⚙️ Multi-threaded Pagination with ORM + SQLite

A modular Python project combining **SQLAlchemy ORM**, **pagination**, and **multi-threading** to process and update large user datasets efficiently. Built with logging, timing decorators, and a clean architecture. User records will be created by the Python package **faker**.

---

## 📚 Table of Contents

- [🗂️ Project Structure](#️-project-structure)
- [🚀 Features](#-features)
- [⚙️ Requirements](#️-requirements)
- [🔧 Setup Instructions](#-setup-instructions)
- [🏃 How to Run](#-how-to-run)
- [🛠️ Customization](#️-customization)
- [🧪 Sample Output](#-sample-output)

---

## 🗂️ Project Structure

```
project-root/
│
├── .env                                # Environment variables
├── .gitignore                          # gitignore folders/files config
├── run.py                              # 🚀 Main entry point
├── requirements.txt                    # Python dependencies for the project
├── README.md                           # Project documentation
│
├── src/
│   ├── database_manager/
│   │   ├── db_config.py                # SQLAlchemy DB engine and Base
│   │   ├── models.py                   # User model
│   │   ├── session_handler.py          # Decorator for DB session handling
│   │   └── __init__.py
│   │
│   ├── global_logger/
│   │   ├── logger_config.py            # Custom logger setup
│   │   └── __init__.py
│   │
│   ├── service/
│   │   ├── multi_threading_service.py  # ThreadPoolExecutor logic
│   │   ├── pagination_service.py       # Paginated CRUD operations
│   │   └── __init__.py
│   │
│   ├── user_database/
│   │   └── users.db                    # SQLite DB file
│   │
│   └── utils/
│       ├── constants.py                # Shared constants like PAGE_SIZE
│       ├── time_calculation.py         # Decorator for measuring execution time
│       └── __init__.py
│
├── .vscode/
│   └── launch.json                     # VSCode run/debug config
└── .venv/                              # Virtual environment (not checked in)
```

---

## 🚀 Features

- ✅ Clean modular architecture
- ✅ SQLAlchemy + SQLite ORM
- ✅ Pagination logic (customizable)
- ✅ Multi-threading using `ThreadPoolExecutor`
- ✅ Logger with thread-specific info
- ✅ Decorator to log execution time
- ✅ Easy to customize and extend

---

## ⚙️ Requirements

- Python 3.8 or above
- Virtual environment (optional but recommended)

```bash
pip install -r requirements.txt
```

---

## 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/janakar-12/multi_threading_with_pagination.git
cd multi_threading_with_pagination

# (Optional) Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Linux: source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🏃 How to Run Locally

```bash
python run.py
```

Make sure `users.db` exists in `src/user_database/` or gets created on first run.

---

## 🛠️ Customization

| What to Change         | File                                 | Variable Name          |
|------------------------|--------------------------------------|------------------------|
| Page size              | `src/utils/constants.py`             | `PAGE_SIZE`            |
| Max threads            | `src/utils/constants.py`             | `MAX_WORKERS`          |
| Fake users count       | `src/utils/constants.py`             | `FAKE_USER_COUNT`      |
| Logging Formatting     | `src/global_logger/logger_config.py` | `formatter`            |
| Logging Level          | `.env`                               | `ENV`                  |
| Timing decorator       | `src/utils/time_calculation.py`      | `@execution_timer`     |
| DB path                | `src/database_manager/db_config.py`  | `DB_FILE_PATH`         |

---

## 🧪 Sample Output

```bash
[INFO] 2025-06-15 01:23:43 - __main__ - Faker started creating fake users...
[INFO] 2025-06-15 01:23:44 - src.utils.time_calculation - Finished 'add_fake_users' in 0.1775 seconds.
[INFO] 2025-06-15 01:23:44 - src.service.multi_threading_service - Running threaded update...
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_0 is processing page 1
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_1 is processing page 2
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_2 is processing page 3
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_0 finished page 1
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_3 is processing page 4
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_4 is processing page 5
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_1 finished page 2
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_3 finished page 4
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_2 finished page 3
[INFO] 2025-06-15 01:23:44 - src.service.pagination_service - PageWorker_Thread_4 finished page 5
[INFO] 2025-06-15 01:23:44 - src.utils.time_calculation - Finished 'initiate_multi_threading' in 0.5075 seconds.
```

---

> Built with ❤️ by [Janakar]
