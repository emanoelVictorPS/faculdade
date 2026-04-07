a=input("digite algo: ")

print(type(a))

try:
    numero=int(a)
    numero=numero*2
    print(numero)
except ValueError:
    try:
        numero=float(a)
        numero=numero/2
        print(numero)
    except ValueError:
        print("tipo inválido")