from random import randint
tentativi1=0
a=1
b=2

while a != b:
    a= randint(1,6)
    b= randint(1,6)
    tentativi1+=1
    print(a,b)
print("Tentativi usati",tentativi1)

tentativi2=0
a=1
b=2
while a != b:
    a= randint(1,6)
    b= randint(1,6)
    tentativi2+=1
    print(a,b)
print("Tentativi usati",tentativi2)
if tentativi1 < tentativi2:
    print("Ha vinto il",tentativi1)
else:
    print("Ha vinto il",tentativi2)
