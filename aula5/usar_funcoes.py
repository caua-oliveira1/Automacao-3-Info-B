import aula4.funcao as funcao

funcao.imprimir('digite o numero 1: ')
nu1 = funcao.ler()
funcao.pulaLinha()
funcao.pulaLinha()

funcao.imprimir('digite o numero 2: ')
nu2 = funcao.ler()

resposta = funcao.somar(nu1, nu2)
funcao.imprimir(f'resultado = {resposta}')