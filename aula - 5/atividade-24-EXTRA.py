a=int(input("digite um número: "))

if 1<a<100:
    if a%2==0:
        print("par no intervalo")
    else:
        print("ímpar no intervalo")
else:
    print("fora do intervalo")