Initial commit
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if(idade < 18):
    autorizacao = input("Os pais autorizaram a viagem? [SIM/NAO]: ")

print (f"Realizando o embarque de {nome}")