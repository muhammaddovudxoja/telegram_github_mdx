🤖 Region & District Admin Telegram Bot

A Telegram admin panel bot built with Python and Aiogram 3 that allows managing regions and districts directly from Telegram using inline buttons.

---

🚀 About Project

This bot provides an interactive admin interface where users can:

- View regions
- View districts by selected region
- Update district names
- Delete districts
- Manage data dynamically via Telegram

The project demonstrates real-world CRUD operations using FSM and inline keyboards.

---

⚙️ Features

✅ Region list display
✅ District filtering by region
✅ Inline keyboard navigation
✅ District update (FSM based)
✅ District delete functionality
✅ Database integration
✅ Async Telegram Bot architecture

---

🛠 Tech Stack

- Python 3.10+
- Aiogram 3
- FSM (Finite State Machine)
- Async Programming
- SQLite / PostgreSQL
- Inline Keyboard UI

---

📂 Project Structure

telegram_github_mdx/
│
├── main.py
├── config/
├── models/
├── database/
├── .env
├── .gitignore
└── README.md

---

🔐 Environment Setup

Create a ".env" file in the root directory:

TELEGRAM_BOT_TOKEN=your_bot_token_here

---

📦 Installation

Clone repository

git clone https://github.com/muhammaddovudxoja/telegram_github_mdx.git

Create virtual environment

python -m venv .venv

Activate environment

source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

---

▶️ Run Bot

python main.py

---

🧠 Bot Workflow

/start
   ↓
Regions
   ↓
District List
   ↓
✏️ Update | ❌ Delete
   ↓
Database Updated

---

📸 Functionality

- Dynamic inline buttons
- FSM state management
- Real-time message update
- Admin CRUD operations inside Telegram

---

👨‍💻 Author

Muhammad Dovud
Python Backend Developer
PDP Academy Student

---

⭐ Future Improvements

- Admin authentication
- Pagination system
- Redis FSM storage
- Docker support
- REST API integration