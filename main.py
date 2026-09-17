from flask import Flask, render_template, request, redirect, url_for, session
from SCRIPT.db import db
from SCRIPT.system import user_log, novo_feedback, preparar_banco_feedback, listar_feedbacks, editar_feedback, excluir_feedback
from SCRIPT.models import Usuarios, Feedback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave-simples'
db.init_app(app)

# --- HOME ---
@app.route('/')
def home():
    feedbacks = listar_feedbacks()
    return render_template('homepage.html', feedbacks=feedbacks)

# --- TELA LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
            nome = request.form['user']
            senha = request.form['senha']
            usuario = Usuarios.query.filter_by(nome=nome, senha=senha).first()
            if usuario:
                session['usuario_id'] = usuario.id
                session['usuario_nome'] = usuario.nome
                return redirect(url_for('home'))
            return redirect(url_for('login'))
    return render_template('login.html',)

# --- TELA CADASTRO ---
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['user']
        senha = request.form['senha']
        user_log(nome, senha)
        return redirect(url_for('login'))
    return render_template('cadastro.html',)

# --- TELA FEEDBACK ---
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        assunto = request.form['assuntoForm']
        resenha = request.form['resenhaForm']
        local = request.form['localForm']
        data = request.form['dataForm']
        status = request.form['statusForm']
        novo_feedback(session['usuario_id'], session['usuario_nome'], assunto, resenha, local, data, status)
        return redirect(url_for('home'))
    return render_template('feedback.html',)

# --- EDITAR FEEDBACK ---
@app.route('/feedback/<id_feedback>/editar', methods=['GET', 'POST'])
def editar_feedback_rota(id_feedback):
    feedback = Feedback.query.get_or_404(id_feedback)

    if request.method == 'POST':
        usuario = request.form['user']
        senha = request.form['senha']
        dono = Usuarios.query.filter_by(id=feedback.usuario_id, nome=usuario, senha=senha).first()

        if dono:
            assunto = request.form['assuntoForm']
            resenha = request.form['resenhaForm']
            local = request.form['localForm']
            data = request.form['dataForm']
            status = request.form['statusForm']
            editar_feedback(feedback, assunto, resenha, local, data, status)
            return redirect(url_for('home'))

        return redirect(url_for('editar_feedback_rota', id_feedback=id_feedback))

    return render_template('editar_feedback.html', feedback=feedback)


# --- EXCLUIR FEEDBACK ---
@app.route('/feedback/<id_feedback>/excluir', methods=['GET', 'POST'])
def excluir_feedback_rota(id_feedback):
    feedback = Feedback.query.get_or_404(id_feedback)

    if request.method == 'POST':
        usuario = request.form['user']
        senha = request.form['senha']
        dono = Usuarios.query.filter_by(id=feedback.usuario_id, nome=usuario, senha=senha).first()

        if dono:
            excluir_feedback(feedback)
            return redirect(url_for('home'))

        return redirect(url_for('excluir_feedback_rota', id_feedback=id_feedback))

    return render_template('excluir_feedback.html', feedback=feedback)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        preparar_banco_feedback()
    app.run()
