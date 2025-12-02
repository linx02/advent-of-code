with open("input.txt", "r") as f:
    data = f.read()

s = 0
for r in data.strip().split(","):
    r1, r2 = r.split("-")
    for i in range(int(r1), int(r2) + 1):
        if len(str(i)) % 2 != 0:
            continue
        i1, i2 = str(i)[:int(len(str(i)) / 2)], str(i)[int(len(str(i)) / 2):]
        if i1 == i2:
            s += i

print(s)