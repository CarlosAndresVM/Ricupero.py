from random import randint
tentativi=0
a=1
b=2
while a != b:
    a= randint(1,6)
    b= randint(1,6)
    tentativi+=1
    print(a,b)
print("Tentativi usati",tentativi)
