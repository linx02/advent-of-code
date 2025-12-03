with open("input.txt", "r") as f:
    banks = [l.strip() for l in f.readlines()]

def scan(banks, n):
    r = []
    for b in banks:
        sp = 0
        bp = len(b) - n + 1
        pos_arr = []
        for i in range(n):
            m = sp
            for j in range(sp, bp):
                if b[j] > b[m]: m = j
            pos_arr.append(m)
            bp += 1
            sp = m + 1
        r.append(''.join([str(b[v]) for v in pos_arr]))
    return sum([int(v) for v in r])

def solve1():
    return scan(banks, 2)

def solve2():
    return scan(banks, 12)


print(solve1())
print(solve2())