a=input("digite algo: ")

try:
    numero=int(a)
    if numero%2==0:
        if numero>100:
            print("par alto")
        else:
            print("par baixo")
    else:
        print("ímpar")
except ValueError:
    print("entrada inválida")