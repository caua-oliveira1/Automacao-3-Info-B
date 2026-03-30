continuar = True

while continuar:
    print("Digite o nome do aluno")
    aluno = input()

    resp = int(input("deseja continuar: \n0 para Nao \n1 para Sim "))
    if resp == 0:
        continuar = False