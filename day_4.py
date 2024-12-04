from AoC import AoC
import re

class Day4(AoC):
    def solve1(self):

        self.lines = self.input.split("\n")
        self.line_length = len(self.lines[0])

        counter = 0
        for l, line in enumerate(self.lines):
            for c, char in enumerate(line):
                if char == 'X':
                    counter += self.check_xmas(l, c)

        self.part1 = counter

    def solve2(self):
        self.lines = self.input.split("\n")

        counter = 0
        for l, line in enumerate(self.lines):
            for c, char in enumerate(line):
                if char == 'A':
                    if self.check_mas(l, c): counter += 1

        self.part2 = counter 


    def check_mas(self, l, c):
        indexes = [
            (l-1, c-1), (l-1, c+1),
            (l+1, c-1), (l+1, c+1)
        ]

        check_string = ""

        for il, ic in indexes:
            
            if il < 0 or ic < 0:
                return False

            try:
                check_string += self.lines[il][ic]
            except IndexError:
                return False

        correct = [
            'MMSS', 'SSMM', 'MSMS', 'SMSM'
        ]

        if check_string in correct:
            return True

        return False

    def check_xmas(self, l, c):
        counter = 0
        # Check row straight
        if c + len("xmas") <= self.line_length:
            if self.lines[l][c:c+4] == "XMAS":
                counter += 1
        # Check row backwards
        if c - len("xmas") + 1 >= 0:
            if self.lines[l][c-3:c+1] == "XMAS"[::-1]:
                counter += 1
        # Check column down
        if l + len("xmas") <= len(self.lines):
            tmp_string = ""
            for i in range(len("xmas")):
                tmp_string += self.lines[l+i][c]
            if tmp_string == "XMAS":
                counter += 1
        # Check column up
        if l - len("xmas") + 1 >= 0:
            tmp_string = ""
            for i in range(len("xmas")):
                tmp_string += self.lines[l-i][c]
            if tmp_string == "XMAS":
                counter += 1

        # Check diagonal down-right
        if c + len("xmas") <= self.line_length and l + len("xmas") <= len(self.lines):
            tmp_string = ""
            for i in range(len("xmas")):
                tmp_string += self.lines[l+i][c+i]
            if tmp_string == "XMAS":
                counter += 1

        # Check diagonal down-left
        if c - len("xmas") + 1 >= 0 and l + len("xmas") <= len(self.lines):
            tmp_string = ""
            for i in range(len("xmas")):
                tmp_string += self.lines[l+i][c-i]
            if tmp_string == "XMAS":
                counter += 1

        # Check diagonal up-right
        if c + len("xmas") <= self.line_length and l - len("xmas") + 1 >= 0:
            tmp_string = ""
            for i in range(len("xmas")):
                tmp_string += self.lines[l-i][c+i]
            if tmp_string == "XMAS":
                counter += 1

        # Check diagonal up-left
        if c - len("xmas") + 1 >= 0 and l - len("xmas") + 1 >= 0:
            tmp_string = ""
            for i in range(len("xmas")):
                tmp_string += self.lines[l-i][c-i]
            if tmp_string == "XMAS":
                counter += 1

        return counter

solution = Day4(4)

solution.solve()
solution.print_results()