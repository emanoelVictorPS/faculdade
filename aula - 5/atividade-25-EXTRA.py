a=input("digite algo: ")

print(type(a))

try:
    numero=float(a)
    numero=numero/2
    print(numero)
except ValueError:
    print("não numérico")