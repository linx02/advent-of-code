from AoC import AoC

class Day1(AoC):
    def solve1(self):
        left = []
        right = []

        numbers = [line.strip() for line in self.input.split('\n')]

        for number in numbers:
            left.append(int(number.split()[0]))
            right.append(int(number.split()[1]))

        left.sort()
        right.sort()

        distances = []

        for l, r in zip(left, right):
            distances.append(max(abs(l - r), abs(r - l)))

        self.part1 = sum(distances)

    def solve2(self):
        left = []
        right = []

        numbers = [line.strip() for line in self.input.split('\n')]

        for number in numbers:
            left.append(int(number.split()[0]))
            right.append(int(number.split()[1]))

        left.sort()
        right.sort()

        similiarity_score = 0
        for i in range(len(left)):
            c = 0
            while True:
                if c == len(right):
                    break
                if left[i] == right[c]:
                    similiarity_score += left[i]
                c += 1
            i += 1

        self.part2 = similiarity_score

solution = Day1(1)

solution.solve()
solution.print_results()