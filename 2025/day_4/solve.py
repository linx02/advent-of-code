with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def accessible(i, j):
    global lines
    p = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1)
    ]
    c = 0
    for pos in p:
        x, y = pos
        if j + x < 0 or i + y < 0 or j + x > len(lines[0]) - 1 or i + y > len(lines) - 1: continue
        if lines[i + y][j + x] == '@': c += 1
    return c < 4

a = 0
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == '@':
            if accessible(i, j):
                a += 1

print(a)