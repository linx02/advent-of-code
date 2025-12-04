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

def scan(lines):
    a = 0
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == '@':
                if accessible(i, j):
                    tmp = list(lines[i])
                    tmp[j] = 'x'
                    tmp = ''.join(tmp)
                    lines[i] = tmp
                    a += 1
    return a, lines

def solve1(lines):
    a, lines = scan(lines)
    return a

def solve2(lines):
    a = 0
    while True:
        tmp, lines = scan(lines)
        a += tmp
        if tmp == 0:
            break

    return a

print(solve2(lines))