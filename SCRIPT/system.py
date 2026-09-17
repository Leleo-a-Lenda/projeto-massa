import uuid
from sqlalchemy import text
from .db import db
from .models import Usuarios, Feedback


def preparar_banco_feedback():
    colunas = db.session.execute(text('PRAGMA table_info(feedbacks)')).fetchall()
    nomes_colunas = {coluna[1] for coluna in colunas}

    novas_colunas = {
        'usuario_id': 'VARCHAR(36)',
        'nome_usuario': 'VARCHAR(40)',
        'assunto': 'VARCHAR(100)',
        'resenha': 'TEXT',
        'local': 'VARCHAR(100)',
        'data': 'VARCHAR(20)',
        'status': 'VARCHAR(30)',
    }

    for nome, tipo in novas_colunas.items():
        if nome not in nomes_colunas:
            db.session.execute(text(f'ALTER TABLE feedbacks ADD COLUMN {nome} {tipo}'))

    db.session.commit()


def novo_feedback(usuario_id, nome_usuario, assunto, resenha, local, data, status):
    feedback = Feedback(
        id=str(uuid.uuid4()),
        usuario_id=usuario_id,
        nome_usuario=nome_usuario,
        assunto=assunto,
        resenha=resenha,
        local=local,
        data=data,
        status=status
    )
    db.session.add(feedback)
    db.session.commit()


def user_log(nome, senha):
    novo_user = Usuarios(id=str(uuid.uuid4()), nome=nome, senha=senha)
    db.session.add(novo_user)
    db.session.commit()


def listar_feedbacks():
    return Feedback.query.all()


def editar_feedback(feedback, assunto, resenha, local, data, status):
    feedback.assunto = assunto
    feedback.resenha = resenha
    feedback.local = local
    feedback.data = data
    feedback.status = status
    db.session.commit()



def excluir_feedback(feedback):
    db.session.delete(feedback)
    db.session.commit()
