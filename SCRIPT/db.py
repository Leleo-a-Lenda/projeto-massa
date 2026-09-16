import sqlite3

conexao = sqlite3.connect("consertapd.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS solicitacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    local TEXT NOT NULL,
    descricao TEXT NOT NULL,
    data TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conexao.commit()


def cadastrar(local, descricao, data, status="Pendente"):
    cursor.execute("""
        INSERT INTO solicitacao
        (local, descricao, data, status)
        VALUES (?, ?, ?, ?)
    """, (local, descricao, data, status))

    conexao.commit()
    print("Solicitação cadastrada com sucesso!")


def listar():
    cursor.execute("SELECT * FROM solicitacao")
    solicitacoes = cursor.fetchall()

    if not solicitacoes:
        print("Nenhuma solicitação cadastrada.")
        return

    print("\n===== SOLICITAÇÕES =====")

    for solicitacao in solicitacoes:
        print(
            f"\nID: {solicitacao[0]}"
            f"\nLocal: {solicitacao[1]}"
            f"\nDescrição: {solicitacao[2]}"
            f"\nData: {solicitacao[3]}"
            f"\nStatus: {solicitacao[4]}"
        )


def editar(id, local, descricao, data, status):
    cursor.execute("""
        UPDATE solicitacao
        SET local = ?,
            descricao = ?,
            data = ?,
            status = ?
        WHERE id = ?
    """, (local, descricao, data, status, id))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Solicitação atualizada com sucesso!")
    else:
        print("Solicitação não encontrada.")


def excluir(id):
    cursor.execute("""
        DELETE FROM solicitacao
        WHERE id = ?
    """, (id,))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Solicitação excluída com sucesso!")
    else:
        print("Solicitação não encontrada.")


def filtrar_status(status):
    cursor.execute("""
        SELECT * FROM solicitacao
        WHERE status = ?
    """, (status,))

    solicitacoes = cursor.fetchall()

    if not solicitacoes:
        print("Nenhuma solicitação encontrada.")
        return

    print(f"\n===== STATUS: {status.upper()} =====")

    for solicitacao in solicitacoes:
        print(
            f"\nID: {solicitacao[0]}"
            f"\nLocal: {solicitacao[1]}"
            f"\nDescrição: {solicitacao[2]}"
            f"\nData: {solicitacao[3]}"
            f"\nStatus: {solicitacao[4]}"
        )


while True:

    print("\n================================")
    print("          CONSERTAPD")
    print("================================")
    print("1 - Cadastrar solicitação")
    print("2 - Listar solicitações")
    print("3 - Editar solicitação")
    print("4 - Excluir solicitação")
    print("5 - Filtrar por status")
    print("0 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        local = input("Local: ")
        descricao = input("Descrição: ")
        data = input("Data: ")

        print("\nStatus:")
        print("1 - Pendente")
        print("2 - Em andamento")
        print("3 - Resolvido")

        escolha_status = input("Escolha: ")

        if escolha_status == "1":
            status = "Pendente"
        elif escolha_status == "2":
            status = "Em andamento"
        elif escolha_status == "3":
            status = "Resolvido"
        else:
            status = "Pendente"

        cadastrar(local, descricao, data, status)

    elif opcao == "2":
        listar()

    elif opcao == "3":

        id = int(input("ID da solicitação: "))
        local = input("Novo local: ")
        descricao = input("Nova descrição: ")
        data = input("Nova data: ")
        status = input("Novo status: ")

        editar(id, local, descricao, data, status)

    elif opcao == "4":

        id = int(input("ID da solicitação: "))
        excluir(id)

    elif opcao == "5":

        status = input(
            "Digite o status "
            "(Pendente, Em andamento ou Resolvido): "
        )

        filtrar_status(status)

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida!")

conexao.close()
