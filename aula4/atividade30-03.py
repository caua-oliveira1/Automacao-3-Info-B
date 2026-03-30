usuario = ''
senha = ''

while (usuario != 'admin' or senha != 'admin123'):
    usuario = input("Digite seu Login ")
    senha = input("Digite sua senha ")

    if (usuario == 'admin' and senha == 'admin123'):
        print("bem vindo ao sistema")
