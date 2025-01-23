class AoC:
    def __init__(self, day):
        self.day = day
        self.input = self.get_input()
        self.test_input = self.get_test_input()
        self.part1 = None
        self.part2 = None

    def get_input(self):
        with open(f"input/day_{self.day}.txt") as f:
            return f.read()

    def get_test_input(self):
        with open(f"input/day_{self.day}_test.txt") as f:
            return f.read()

    def solve(self):
        self.solve1()
        self.solve2()

    def solve1(self):
        raise NotImplementedError

    def solve2(self):
        raise NotImplementedError

    def print_results(self):
        print(f"Day {self.day}")
        print(f"Part 1: {self.part1}")
        print(f"Part 2: {self.part2}")