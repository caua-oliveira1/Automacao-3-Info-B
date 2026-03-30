while True:
    try:

        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite o segundo numero: "))
        div = n1 / n2
        print(div)
        break
    
    except ValueError:
        print("o valor digitado e invalido")
    except Exception as e:
        print("deu erro fella",e)