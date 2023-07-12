from random import choice
alunos = []
for i in range(4):
    aluno = input("insira o nome do aluno: ")
    alunos.append(aluno)
escolhido = choice(alunos)
print("o escolhido foi ",escolhido)


