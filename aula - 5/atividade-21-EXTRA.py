a=int(input("digite um número: "))
if a>0:
    if (a%2==0) and (a%3==0):
        print("múltiplo de 2 e 3")
    else:
        print("não atende")
else:
    print("número inválido")