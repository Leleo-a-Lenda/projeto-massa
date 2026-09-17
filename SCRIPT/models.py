from .db import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.String(36), primary_key=True)
    usuario_id = db.Column(db.String(36), nullable=False)
    nome_usuario = db.Column(db.String(40), nullable=False)
    assunto = db.Column(db.String(100), nullable=False)
    resenha = db.Column(db.Text, nullable=False)
    local = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f'<Feedback {self.assunto}>'

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.String(36), primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
