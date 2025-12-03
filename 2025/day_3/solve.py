with open("input.txt", "r") as f:
    banks = [l.strip() for l in f.readlines()]

r = 0
for b in banks:
    b = b[::-1]
    cmp1 = 1
    for pos, b_ in enumerate(b[2:]):
        if b_ >= b[cmp1]: cmp1 = pos + 2
    cmp2 = 0
    for pos, b_ in enumerate(b[1:]):
        if pos + 1 == cmp1: break
        if b_ >= b[cmp2]: cmp2 = pos + 1
    b = b[::-1]
    r += int(str(b[len(b) - cmp1 - 1] + b[len(b) - cmp2 - 1]))

print(r)