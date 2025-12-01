with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def rotate(i, d, v):
    while(v != 0):
        if d == 'L':
            if i - v < 0:
                v -= i + 1
                i = 99
            else:
                i -= v
                break
        elif d == 'R':
            if i + v > 99:
                v -= 99 - i + 1
                i = 0
            else:
                i += v
                break
    return i

i = 50
c = 0
for l in lines:
    d = l[0]
    v = int(l[1:])
    i = rotate(i, d, v)
    if i == 0:
        c += 1

print(c)