import uuid


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


class Cadastro:
    def __init__(self, nome, senha):
        self.id = uuid.uuid4()
        self.nome = nome
        self.senha = senha

def listar_feedbacks():
    pass
