from AoC import AoC

class Day5(AoC):

    def solve1(self):
        rules, updates = self.input.split("\n\n")

        correct_updates = []

        updates = updates.split("\n")
        for update in updates:
            update = [int(x) for x in update.split(",")][::-1]

            rule_map = {}

            r = rules.split("\n")
            for u in update:
                rule_map[u] = []
            for rule in r:
                x, y = rule.split("|")
                if int(x) in update and int(y) in update:
                    rule_map[int(y)].append(int(x))

            if self.check_update(update, rule_map):
                correct_updates.append(update)

        self.part1 = sum([update[int(len(update)/2)] for update in correct_updates])

    def solve2(self):
        rules, updates = self.input.split("\n\n")

        incorrect_updates = []
        corrected_updates = []

        updates = updates.split("\n")
        for update in updates:
            update = [int(x) for x in update.split(",")][::-1]

            rule_map = {}

            r = rules.split("\n")
            for u in update:
                rule_map[u] = []
            for rule in r:
                x, y = rule.split("|")
                if int(x) in update and int(y) in update:
                    rule_map[int(y)].append(int(x))

            if not self.check_update(update, rule_map):
                corrected_updates.append(sorted(rule_map, key=lambda i: len(rule_map[i])))

        self.part2 = sum([update[int(len(update)/2)] for update in corrected_updates])


    def check_update(self, update, rule_map):
       for i, u in enumerate(update):
                for c in rule_map[u]:
                    if c in update[i:]:
                        continue
                    else:
                        return False
                if i == len(update)-1:
                    return True

solution = Day5(5)
solution.solve()

solution.print_results()