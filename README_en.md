# mini-ec-fastapi

A lightweight e-commerce prototype built with **FastAPI** and **HTMX**.

This project demonstrates a minimal and modern approach to building an EC site using Python backend and asynchronous UI components with HTMX.

---

## 🚀 Setup Instructions

```bash
# Activate virtual environment (create one if needed)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
🛒 Features
Product list display

Add/remove items to/from cart (via HTMX async)

Checkout confirmation screen

Modular CSS components (header, item, button)

📁 Project Structure
css
コピーする
編集する
app/
├── main.py
├── db.py
├── models.py
├── templates/
│   ├── index.html
│   ├── cart.html
│   ├── checkout.html
│   └── partials/
│       ├── header.html
│       └── footer.html
├── static/
│   └── css/
│       ├── base.css
│       ├── header.css
│       ├── item.css
│       └── button.css

📦 Tech Stack
Python 3.x
FastAPI
HTMX
Jinja2
HTML / CSS

🌐 Author
Created by Daisuke Hagihara

Feel free to fork, clone, or adapt for your own minimal EC projects.