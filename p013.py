from random import randint
a= randint(1,6)
somma=0
for x in range(1,10,1):
    a=randint(1,6)
    somma+=a 
    print(a)
print("La somma è",somma)