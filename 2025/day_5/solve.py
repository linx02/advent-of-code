with open("input.txt", "r") as f:
    switch = False
    ids = []
    ranges = []
    for l in f.readlines():
        if l == '\n': switch = True
        if switch: ids.append(l.strip())
        else: ranges.append(l.strip())
    ids = ids[1:]

def fresh(i, r):
    l, h = r.split('-')
    l = int(l)
    h = int(h)
    i = int(i)
    return i >= l and i <= h

a = 0
for i in ids:
    for r in ranges:
        if fresh(i, r):
            a += 1
            break

print(a)