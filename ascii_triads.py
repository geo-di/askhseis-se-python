import random
import string

print("Please type the file name with its extension!")

# diabazei to onoma toy arxeiou kai to anoigei
text = input()
f = open(text)
f = f.read()

# apo to keimeno krataei mono grammata kena kai apostrofous pou einai anamesa se grammata
new = []
for i in range(len(f)):
    if f[i] in string.ascii_letters or f[i] in string.whitespace or \
            (f[i] == "'" and (f[i + 1] in string.ascii_letters) and (f[i - 1] in string.ascii_letters)):
        new += f[i]

# kanei ti lista me xarakthres string kanei ta grammata peza kai xwrizei tis lekseis
f = "".join(new)
f = f.lower()
f = f.split()

# xwrizei to keimeno se triades leksewn
k = 0
table = []
x = round(len(f) // 3)
for i in range(x):
    new = []
    for j in range(3):
        new.append(f[k])
        k += 1
    table.append(new)

# anakateuei tis triades kai dialegei mia
random.shuffle(table)
current = table.pop(0)

# psaxnei triades mexri na einai to keimeno panw apo 200 lekseis h na teleiwsoun oi triades
while len(current) < 200 or len(table) > 0:
    search = False
    random.shuffle(table)
    for i in table:
        if current[-2] == i[0] and current[-1] == i[1]:
            current.append(i[0])
            current.append(i[1])
            current.append(i[2])
            table.remove(i)
            search = True
            break

    # an den uparxei triada teleiwnei h epanalipsh
    if not search:
        break

# ektypwnei
current = " ".join(current)
print(current)
