from flask import Flask, render_template, request, jsonify
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
app = Flask(__name__, template_folder=str(ROOT / 'frontend' / 'templates'), static_folder=str(ROOT / 'frontend' / 'static'))
app.secret_key = 'change-this-for-production'

@app.get('/')
def home():
    return render_template('index.html')

@app.post('/contact')
def contact():
    data = request.get_json(silent=True) or request.form
    name = str(data.get('name', '')).strip()
    email = str(data.get('email', '')).strip()
    message = str(data.get('message', '')).strip()
    if not name or not email or not message:
        return jsonify(ok=False, message='Please fill in all fields.'), 400
    # Demo only: submissions are not emailed or saved to a database.
    return jsonify(ok=True, message=f'Thanks, {name}! Your demo message was received.')

@app.get('/health')
def health():
    return jsonify(status='ok')

if __name__ == '__main__':
    app.run(debug=True)
