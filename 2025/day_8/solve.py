class Playground():
    def __init__(self, junction_boxes):
        self.junction_boxes = junction_boxes
        self.circuits = [[jb] for jb in self.junction_boxes]

    def connect(self, i, j):
        box_1 = self.junction_boxes[i]
        box_2 = self.junction_boxes[j]
        p1 = p2 = None
        for _, circuit in enumerate(self.circuits):
            if p1 and p2: break
            if box_1 in circuit:
                p1 = _
            if box_2 in circuit:
                p2 = _
        if p1 == p2: return
        self.circuits.append(self.circuits[p1] + self.circuits[p2])
        del self.circuits[max(p1, p2)]
        del self.circuits[min(p1, p2)]

    def get_distance(self, i, j):
        box_1 = self.junction_boxes[i]
        box_2 = self.junction_boxes[j]

        dx = box_1.x - box_2.x
        dy = box_1.y - box_2.y
        dz = box_1.z - box_2.z

        return dx*dx + dy*dy + dz*dz

class JunctionBox():
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

with open('input.txt', 'r') as f:
    tmp = [l.strip() for l in f.readlines()]
    jbs = []
    for i, pos in enumerate(tmp):
        x, y, z = pos.split(',')
        jbs.append(JunctionBox(i, int(x), int(y), int(z)))

playground = Playground(jbs)

edges = []
n_boxes = len(playground.junction_boxes)

for i in range(n_boxes):
    for j in range(i + 1, n_boxes):
        d = playground.get_distance(i, j)
        edges.append((d, i, j))

edges.sort(key=lambda e: e[0])

connections = 0
idx = 0
n = 1000

while connections < n and idx < len(edges):
    dist, i, j = edges[idx]
    idx += 1

    playground.connect(i, j)
    connections += 1

s_arr = sorted(playground.circuits, key=lambda circuit: len(circuit))
s_arr = s_arr[::-1]
a = len(s_arr[0])*len(s_arr[1])*len(s_arr[2])
print(a)