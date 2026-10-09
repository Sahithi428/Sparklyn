# Sparklyn — Simple Flask Website

A small full-stack starter project with a Flask backend and separate HTML, CSS, and JavaScript files.

## Run in VS Code (Windows)

1. Extract this ZIP and open the `Sparklyn-Simple` folder in VS Code.
2. Open Terminal → New Terminal.
3. (Optional but recommended) Create a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
4. Install Flask:
   ```powershell
   py -m pip install -r requirements.txt
   ```
5. Start the website:
   ```powershell
   py backend/app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

The `/health` endpoint returns a simple backend status at `http://127.0.0.1:5000/health`.

**Note:** The contact form is a demo. It validates submissions and shows a confirmation, but does not email or save messages.
