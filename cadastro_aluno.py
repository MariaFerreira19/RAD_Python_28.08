import os

class Aluno:
    def __init__(self, nome, email, curso):
        self.nome = nome
        self.email = email
        self.curso = curso

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")
    
    aluno = Aluno(nome, email, curso)
    
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{aluno.nome};{aluno.email};{aluno.curso}\n")
    
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    if not os.path.exists("alunos.txt"):
        print("Nenhum aluno cadastrado ainda.")
        return
    
    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            nome, email, curso = linha.strip().split(";")
            print(f"Nome: {nome}, Email: {email}, Curso: {curso}")

def buscar_aluno_por_nome():
    nome_busca = input("Digite o nome do aluno a ser buscado: ")
    
    encontrados = []
    
    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            nome, email, curso = linha.strip().split(";")
            if nome_busca.lower() in nome.lower():
                encontrados.append((nome, email, curso))
    
    if encontrados:
        print("Alunos encontrados:")
        for nome, email, curso in encontrados:
            print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
    else:
        print("Nenhum aluno encontrado com esse nome.")

def main():
    while True:
        print("\nOpções:")
        print("1. Cadastrar um novo aluno")
        print("2. Listar os alunos cadastrados")
        print("3. Buscar um aluno pelo nome")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == "1":
            cadastrar_aluno()
        elif escolha == "2":
            listar_alunos()
        elif escolha == "3":
            buscar_aluno_por_nome()
        elif escolha == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
