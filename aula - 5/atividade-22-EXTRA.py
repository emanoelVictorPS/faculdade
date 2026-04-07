a=input("digite algo: ")

try:
    numero=int(a)
    if numero>10:
        print("alto")
    else:
        print("baixo")
except ValueError:
    print("entrada inválida")


