a=float(input("digite um número: "))
b=float(input("digite outro número: "))
c=float(input("digite mais um número: "))

a=a%3
b=b%3
c=c%3

if a>b>c:
    print("a sequencia decrescente é :",a,b,c)
if a>c>b:
    print("a sequencia decrescente é :",a,c,b)
if b>a>c:
    print("a sequencia decrescente é :",b,a,c)
if b>c>a:
    print("a sequencia decrescente é :",b,c,a)
if c>a>b:
    print("a sequencia decrescente é :",c,b,a)
if c>b>a:
    print("a sequencia decrescente é :",c,b,a)