with open('input.txt') as f:
    lines = f.readlines()

def solve1():
    global lines
    a = 0
    lines_ = [l.strip() for l in lines]
    problems = [[] for n in lines_[0].split()]

    for i in range(len(lines_[0].split())):
        for j in range(len(lines_)):
            problems[i].append(lines_[j].split()[i])

    for p in problems:
        o = p[-1]
        p = p[:-1]
        e = o.join(p)
        a += eval(e)
    return a

def solve2():
    global lines
    a = 0
    problems = [[] for i in range(len(lines[0].split()))]
    cols = []

    for i in range(len(lines[0]) - 1):
        col = []
        for j in range(len(lines)):
            col.append(lines[j][i])
        cols.append(col)

    cols = cols[::-1]

    i = 0
    eq = []
    for j, col in enumerate(cols):
        c = ''.join(col).strip()
        if c == '': continue
        if c[-1] in ['+', '*', '/', '-']:
            o = c[-1]
            c = c[:-1]
            eq.append(c)
            problems[i] = o.join(eq)
            problems[i] = problems[i].strip()
            eq = []
            i += 1
            continue
        eq.append(c)

    for p in problems:
        a += eval(p)
    return a
    

print(solve1())
print(solve2())