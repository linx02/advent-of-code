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

def solve1():
    global ranges
    a = 0
    for i in ids:
        for r in ranges:
            if fresh(i, r):
                a += 1
                break
    return a

def solve2():
    global ranges
    a = 0
    ranges = sorted(ranges, key=lambda r: int(r.split('-')[0]))
    m = 0
    for r in ranges:
        l, h = r.split('-')
        l = int(l)
        h = int(h)
        if m > l:
            l = m
        if m > h:
            continue
        if m == l:
            a -= 1
        m = h
        a += h-l+1
    return a

print(solve1())
print(solve2())