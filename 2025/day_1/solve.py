with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def rotate(i, d, v):
    c1 = 0
    c2 = 0
    while v != 0:
        if d == 'L':
            i -= 1
            v -= 1
            if i == -1: i = 99
            if v == 0 and i == 0:
                c1 += 1
                break
            if v != 0 and i == 0: c2 += 1
        if d == 'R':
            i += 1
            v -= 1
            if i == 100: i = 0
            if v == 0 and i == 0:
                c1 += 1
                break
            if v != 0 and i == 0: c2 += 1
    return i, c1, c2


def solve1():
    i = 50
    c = 0
    for l in lines:
        d = l[0]
        v = int(l[1:])
        i, c1, c2 = rotate(i, d, v)
        c += c1
    return c

def solve2():
    i = 50
    c = 0
    for l in lines:
        d = l[0]
        v = int(l[1:])
        i, c1, c2 = rotate(i, d, v)
        c += c1 + c2
    return c

print(solve1())
print(solve2())