with open("input.txt", "r") as f:
    data = f.read()

def solve1():
    s = 0
    for r in data.strip().split(","):
        r1, r2 = r.split("-")
        for i in range(int(r1), int(r2) + 1):
            if len(str(i)) % 2 != 0:
                continue
            i1, i2 = str(i)[:int(len(str(i)) / 2)], str(i)[int(len(str(i)) / 2):]
            if i1 == i2:
                s += i
    return s

def solve2():
    s = 0
    for r in data.strip().split(","):
        r1, r2 = r.split("-")
        for i in range(int(r1), int(r2) + 1):
            is1 = str(i)
            j = 1
            while j <= int(len(is1) / 2):
                p = is1[:j]
                t = int(len(is1) / j)
                is2 = p*t
                if is1 == is2:
                    s += i
                    break
                j += 1
    return s

print(solve1())
print(solve2())