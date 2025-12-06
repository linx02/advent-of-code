with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

problems = [[] for n in lines[0].split()]

for i in range(len(lines[0].split())):
    for j in range(len(lines)):
        problems[i].append(lines[j].split()[i])

a = 0
for p in problems:
    o = p[-1]
    p = p[:-1]
    e = o.join(p)
    a += eval(e)

print(a)