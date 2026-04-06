from aula4.funcao import ler, imprimir, pulaLinha, somar

imprimir('digite o numero 1: ')
nu1 = ler()
pulaLinha()
pulaLinha()

imprimir('digite o numero 2: ')
nu2 = ler()

resposta = somar(nu1, nu2)
imprimir(f'resultado = {resposta}')