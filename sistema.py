class Aluno:
    def __init__(self, matricula, nome, idade, curso, nota):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __str__(self):
        return (f"Matrícula: {self.matricula} | Nome: {self.nome} | "
                f"Idade: {self.idade} | Curso: {self.curso} | Nota: {self.nota}")

alunos = []

def menu():
    print("\n===== MENU DO CRUD DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos (tabela)")
    print("3 - Atualizar aluno")
    print("4 - Remover aluno")
    print("5 - Buscar aluno por matrícula")
    print("8 - Salvar os dados cadastrados")
    print("9 - Carregar dados de arquivo")
    print("0 - Sair")

def cadastrar_aluno():
    matricula = input("📄 Digite o número de matrícula 📄: ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    aluno = Aluno(matricula, nome, idade, curso, nota)
    alunos.append(aluno)
    print("✅ Aluno cadastrado com sucesso! ✅")

def listar_alunos():
    if alunos:
        print("\n📋 TABELA DE ALUNOS:")
        print(f"| {'Matrícula':<10} | {'Nome':<20} | {'Idade':<5} | {'Curso':<25} | {'Nota':<5} |")
        print("-" * 78)
        for aluno in alunos:
            print(f"| {aluno.matricula:<10} | {aluno.nome:<20} | {aluno.idade:<5} | {aluno.curso:<25} | {aluno.nota:<5.1f} |")
    else:
        print("❌ Nenhum aluno cadastrado.")

def atualizar_dados():
    matricula_nova = input("Digite a matrícula do aluno a ser atualizado: ")
    aluno = procurar_por_matricula(matricula_nova)
    if aluno:
        aluno.nome = input("Novo nome: ")
        aluno.idade = int(input("Nova idade: "))
        aluno.curso = input("Novo curso: ")
        aluno.nota = float(input("Nova nota: "))
        print("✅ Aluno atualizado com sucesso! ✅")
    else:
        print("❌ Matrícula não encontrada! ❌")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno a ser removido: ")
    aluno = procurar_por_matricula(matricula)
    if aluno:
        alunos.remove(aluno)
        print("✅ Aluno removido com sucesso! ✅")
    else:
        print("❌ Aluno não encontrado. ❌")

def procurar_por_matricula(matricula):
    for aluno in alunos:
        if aluno.matricula == matricula:
            return aluno
    return None

def buscar_por_matricula():
    matricula = input("🔎 Digite a matrícula para buscar: ")
    aluno = procurar_por_matricula(matricula)
    if aluno:
        print("✅ Aluno encontrado:")
        print(aluno)
    else:
        print("❌ Matrícula não encontrada. ❌")

def salvar_dados_em_arquivo(nome_arquivo="alunos.txt"):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            # Cabeçalho da tabela
            arquivo.write("📋 TABELA DE ALUNOS:\n")
            arquivo.write(f"| {'Matrícula':<10} | {'Nome':<20} | {'Idade':<5} | {'Curso':<25} | {'Nota':<5} |\n")
            arquivo.write("-" * 78 + "\n")

            # Dados de cada aluno
            for aluno in alunos:
                linha = f"| {aluno.matricula:<10} | {aluno.nome:<20} | {aluno.idade:<5} | {aluno.curso:<25} | {aluno.nota:<5.1f} |\n"
                arquivo.write(linha)
        print("💾 Dados salvos em formato de tabela com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")

def carregar_dados_de_arquivo(nome_arquivo="alunos.txt"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                # Ignora linhas vazias ou de cabeçalho/separação
                if not linha or linha.startswith("📋") or linha.startswith("| Matrícula") or linha.startswith("-"):
                    continue

                # Remove bordas e divide a linha por '|'
                partes = linha.strip("|").split("|")
                if len(partes) != 5:
                    continue

                matricula = partes[0].strip()
                nome = partes[1].strip()
                idade = int(partes[2].strip())
                curso = partes[3].strip()
                nota = float(partes[4].strip())

                aluno = Aluno(matricula, nome, idade, curso, nota)
                alunos.append(aluno)

        print("📂 Dados carregados com sucesso a partir da tabela!")
    except FileNotFoundError:
        print("🔍 Arquivo de dados não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")

def executar_menu():
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
        elif opcao == "5":
            buscar_por_matricula()
        elif opcao == "8":
            salvar_dados_em_arquivo()
        elif opcao == "9":
            carregar_dados_de_arquivo()
        elif opcao == "0":
            print("👋 Encerrando o programa...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    carregar_dados_de_arquivo()
    executar_menu()


