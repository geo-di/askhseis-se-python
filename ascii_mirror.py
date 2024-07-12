print("Please type the file name with its extension!")

# diabazei to onoma toy arxeiou kai to anoigei
text = input()
f = open(text)
f = f.read()

# gemizei me lista me toys katoptrikous xaraktires tou keimenou kai antistrefei th seira tous
mirrored = []
for i in f:
    mirrored.append(chr(128 - ord(i)))
mirrored.reverse()

# printing
print("As a list: ", mirrored)
mirrored = "".join(mirrored)
print("As a string: ")
print(mirrored)
