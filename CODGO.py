#algorítimo de cálculo de salário

a=int(input("digite um número "))
b=int(input("digite outro número "))
c=int(input("digite o último número "))

if a<b and a<c:
    print("o menor é:",a)
if b<a and b<c:
    print("o menor é:",b)
if c<a and c<b:
    print("o menor é:",c)
else:
    print("existem números iguais")