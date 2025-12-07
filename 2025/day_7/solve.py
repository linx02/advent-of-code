with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

pos_map = {i: False for i in range(len(lines[0]))}
a = 0
for l in lines:
    for i, c in enumerate(l):
        if c == 'S':
            pos_map[i] = True
        if c == '^' and pos_map[i] == True:
            pos_map[i] = False
            pos_map[i+1] = True
            pos_map[i-1] = True
            a += 1

print(a)