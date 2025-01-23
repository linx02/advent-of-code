
from AoC import AoC

class Day6(AoC):
        def solve1(self):

            directions = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0)
            ]

            direction_map = {
                "^": directions[0],
                ">": directions[1],
                "v": directions[2],
                "<": directions[3]
            }

            rows = self.input.split("\n")
            columns = [[] for i in range(len(rows))]
            
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    columns[j].append(rows[i][j])

            columns = ["".join(column) for column in columns]

            direction = None
            current_pos = None

            for row in rows:
                if direction != None:
                    break
                for char in row:
                    try:
                        direction = direction_map[char]
                        x = row.index(char)
                        y = rows.index(row)
                        current_pos = (x, y)

                        rows[y] = row[:x] + "." + row[x+1:]
                        columns[x] = columns[x][:y] + "." + columns[x][y+1:]
                        break
                    except KeyError:
                        continue

            step_counter = 1

            while True:
                next_x = current_pos[0] + direction[0]
                next_y = current_pos[1] - direction[1]
                try:
                    if next_x < 0 or next_y < 0:
                        break
                    next_char = columns[next_x][next_y]
                except IndexError:
                    break

                match(next_char):
                    case ".":
                        step_counter += 1
                        current_pos = (next_x, next_y)
                        columns[next_x] = columns[next_x][:next_y] + "x" + columns[next_x][next_y+1:]
                    case "#":
                        direction = directions[(directions.index(direction) + 1) % 4]
                    case "x":
                        current_pos = (next_x, next_y)

            self.part1 = step_counter
    
        def solve2(self):
            pass
            


solution = Day6(6)
solution.solve()

solution.print_results()