import random

# creation of list
print("Type the amount of rows: ")
rows = int(input())
print("Type the amount of columns: ")
cols = int(input())
lst = ["S"] * rows * cols
for i in range(rows * cols // 2):
    lst[i] = "O"
average = 0

for a in range(100):
    # turning list into an array
    random.shuffle(lst)
    k = 0
    table = []
    for i in range(rows):
        new = []
        for j in range(cols):
            new.append(lst[k])
            k += 1
        table.append(new)
    count = 0

    for i in range(rows):
        for j in range(cols):
            if table[i][j] == "S":
                # horizontally
                if j < cols - 2:
                    if table[i][j + 1] == "O" and table[i][j + 2] == "S":
                        count += 1
                if i < rows - 2:
                    # vertically
                    if table[i + 1][j] == "O" and table[i + 2][j] == "S":
                        count += 1
                    # diagonally to the right
                    if j < cols - 2:
                        if table[i + 1][j + 1] == "O" and table[i + 2][j + 2] == "S":
                            count += 1
                    # diagonally to the left
                    if j > 1:
                        if table[i + 1][j - 1] == "O" and table[i + 2][j - 2] == "S":
                            count += 1

    average = average + count / 100

print(average)
