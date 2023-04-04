from random import randint
tentativi=0
a=0
while a < 6:
    a= randint(1,6)
    tentativi+=1
    print(a)
print("Tentativi usati",tentativi)
#deve stampare i tentativi , e cuante volte esce certo numero