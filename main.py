from flask import Flask, render_template, request
app = Flask(__name__)

# --- HOME ---
@app.route('/')
def home():
    return render_template('homepage.html',)

# --- TELA LOGIN ---
@app.route('/login')
def login():
    return render_template('login.html',)

# --- TELA CADASTRO ---
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html',)

# --- TELA FEEDBACK ---
@app.route('/feedback')
def feedback():
    return render_template('feedback.html',)

if __name__ == '__main__':
    app.run()