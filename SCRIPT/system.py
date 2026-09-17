import uuid
from .db import db
from .models import Usuarios

class Feedback:
    def __init__(self, usuario, nota, mensagem):
        self.id = uuid.uuid4()
        self.usuario = usuario
        self.nota = nota
        self.mensagem = mensagem


def novo_feedback(usuario, nota, mensagem):
    feedback = Feedback(usuario, nota, mensagem)
    return feedback

#essas duas por enquanto só quando tiver o banco funcionando:(
def buscar_feedback(id_feedback):
    pass

def user_log(nome, senha):
    id = uuid.uuid4()
    novo_user = Usuarios(nome=nome, senha=senha)
    db.session.add(novo_user)
    db.session.commit()

def listar_feedbacks():
    pass
