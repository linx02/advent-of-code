from AoC import AoC
import re

class Day3(AoC):
    def solve1(self):
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, self.input)

        total = 0
        for match in matches:
            a, b = match.split('(')[1].split(')')[0].split(',')
            total += int(a) * int(b)
        
        self.part1 = total



    def solve2(self):
       pattern = r"mul\(\d+,\d+\)" 

       do = True
       total = 0
       for i in range(len(self.input)):
            if self.input[i:i+len("do()")] == "do()":
                do = True
            elif self.input[i:i+len("don't()")] == "don't()":
                do = False
            else:
                if do:
                    if self.input[i:i+len("mul(")] == "mul(":
                        next_match = re.search(r"mul\(\d+,\d+\)", self.input[i:])
                        if next_match.start() == 0:
                            match = next_match.group()
                            a, b = match.split('(')[1].split(')')[0].split(',')
                            total += int(a) * int(b)

       self.part2 = total

solution = Day3(3)
solution.solve()

solution.print_results()