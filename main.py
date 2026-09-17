from flask import Flask, render_template, request, redirect, url_for
from SCRIPT.db import db
from SCRIPT.system import user_log
from SCRIPT.models import Usuarios, Feedback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'sqlite:///feedbacks.db'
db.init_app(app)

# --- HOME ---
@app.route('/')
def home():
    return render_template('homepage.html',)

# --- TELA LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
            nome = request.form['user']
            senha = request.form['senha']
            return redirect(url_for('home'))
    return render_template('login.html',)

# --- TELA CADASTRO ---
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['user']
        senha = request.form['senha']
        user_log(nome, senha)
        return redirect(url_for('home'))
    return render_template('cadastro.html',)

# --- TELA FEEDBACK ---
@app.route('/feedback')
def feedback():
    return render_template('feedback.html',)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()