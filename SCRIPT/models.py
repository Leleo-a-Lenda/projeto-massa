from db import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.nome}>'

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
