from AoC import AoC

class Day1(AoC):

    def setup(self):
        self.left = []
        self.right = []

        numbers = [line.strip() for line in self.input.split('\n')]

        for number in numbers:
            self.left.append(int(number.split()[0]))
            self.right.append(int(number.split()[1]))

        self.left.sort()
        self.right.sort()

    def solve1(self):
        self.setup()

        distances = []

        for l, r in zip(self.left, self.right):
            distances.append(max(abs(l - r), abs(r - l)))

        self.part1 = sum(distances)

    def solve2(self):
        self.setup()

        similiarity_score = 0
        for i in range(len(self.left)):
            c = 0
            while True:
                if c == len(self.right):
                    break
                if self.left[i] == self.right[c]:
                    similiarity_score += self.left[i]
                c += 1
            i += 1

        self.part2 = similiarity_score

solution = Day1(1)

solution.solve()
solution.print_results()