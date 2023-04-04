#estrarre 10 numeri in modo randomico e stampare solo quelli maggiori di 50
from random import randint
i=0
while i<10:
    i=0
    for x in range(1,10,1):
        a=randint(10,90)
        if a > 50:
            i+=1
            print(a)      
print("numeri",i)
 