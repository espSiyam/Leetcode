operations = ["++X","++X","X++"]
x = 0

for i in range(len(operations)):
    if (operations[i] == "X++") or (operations[i] == "++X"):
        x += 1
    if (operations[i] == "X--") or (operations[i] == "--X"):
        x -= 1

print(x)