from AoC import AoC

class Day2(AoC):
    
    def solve1(self):
        lines = [line.strip() for line in self.input.split('\n')]

        safe_reports = 0
        for line in lines:
            numbers = [int(num) for num in line.split()]
            if self.test_safe(numbers):
                safe_reports += 1
                continue
        
        self.part1 = safe_reports

    def solve2(self):
        lines = [line.strip() for line in self.input.split('\n')]

        safe_reports = 0
        for line_index, line in enumerate(lines):
            numbers = [int(num) for num in line.split()]
            if self.test_safe(numbers):
                safe_reports += 1
                continue

            expanded_numbers = []

            for i in range(len(numbers)):
                tmp = numbers.copy()
                tmp.pop(i)
                expanded_numbers.append(tmp)

            for expanded in expanded_numbers:
                if self.test_safe(expanded):
                    safe_reports += 1
                    break
        
        self.part2 = safe_reports

    def test_safe(self, numbers):
        increasing = numbers[0] < numbers[1]

        for i in range(len(numbers) - 1):
            if increasing:
                if numbers[i] >= numbers[i + 1]:
                    return False
                elif numbers[i + 1] - numbers[i] > 3:
                    return False
            elif not increasing:
                if numbers[i] <= numbers[i + 1]:
                    return False
                elif numbers[i] - numbers[i + 1] > 3:
                    return False
            if i == len(numbers) - 2:
                return True

solution = Day2(2)

solution.solve()
solution.print_results()