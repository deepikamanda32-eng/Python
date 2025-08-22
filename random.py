import random
l=[]
while len(l)<=5:
    a=random.randint(1,10)
    if a not in l:
        l.append(a)
print(l)        