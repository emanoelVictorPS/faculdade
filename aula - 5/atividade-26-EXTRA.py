a=int(input("digite um número: "))

if a>0:
    if a<10:
        print("pequeno")
    if 10<=a<=100:
        print("médio")
    if a>100:
        print("grande")
else:
    print("negativo ou zero")