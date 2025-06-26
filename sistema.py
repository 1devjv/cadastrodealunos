class Aluno:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Matrícula: {self.matricula} | Nome: {self.nome} | Idade: {self.idade}"


alunos = []


def menu():
    print("\n===== MENU DO CRUD DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Remover aluno")
    print("0 - Sair")


def cadastrar_aluno():
    matricula = input("📄 Digite o número de matrícula 📄: ")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    aluno = Aluno(matricula, nome, idade)  # ✅ Corrigido
    alunos.append(aluno)
    print("✅ Aluno cadastrado com sucesso! ✅")


def listar_alunos():
    if alunos:
        for aluno in alunos:
            print(aluno)
    else:
        print("❌ Nenhum aluno cadastrado. ❌")


def atualizar_dados():
    matricula_nova = input("Digite a matrícula do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno.matricula == matricula_nova:
            aluno.nome = input("Novo nome: ")
            aluno.idade = input("Nova idade: ")
            print("✅ Aluno atualizado com sucesso! ✅")
            return
    print("❌ Matrícula não encontrada! ❌")


def remover_aluno():
    matricula = input("Digite a matrícula do aluno a ser removido: ")
    for aluno in alunos:
        if aluno.matricula == matricula:
            alunos.remove(aluno)
            print("✅ Aluno removido com sucesso! ✅")
            return
    print("❌ Aluno não encontrado. ❌")


# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        atualizar_dados()
    elif opcao == "4":
        remover_aluno()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("❌ Opção inválida! Tente novamente! ❌")