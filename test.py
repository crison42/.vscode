from queue import Queue


class Puzzle:
    def __init__(self, state):
        self.state = state
        self.empty = state.index(" ")
        self.target = "12345678 "
        self.directions = [-3, 3, -1, 1]  # 上下左右

    def is_solvable(self):
        inv_count = 0
        for i in range(len(self.state)):
            for j in range(i + 1, len(self.state)):
                if (
                    self.state[i] != " "
                    and self.state[j] != " "
                    and self.state[i] > self.state[j]
                ):
                    inv_count += 1
        return inv_count % 2 == 0

    def is_solved(self):
        return self.state == self.target

    def move_empty(self, direction):
        new_empty = self.empty + direction
        if new_empty < 0 or new_empty >= len(self.state):
            return None
        if direction == -1 and self.empty % 3 == 0:
            return None
        if direction == 1 and new_empty % 3 == 0:
            return None
        new_state = list(self.state)
        new_state[self.empty], new_state[new_empty] = (
            new_state[new_empty],
            new_state[self.empty],
        )
        return Puzzle("".join(new_state))

    def print_puzzle(self):
        for i in range(0, 9, 3):
            print(self.state[i : i + 3].replace("", " | ")[2:-2])
            if i < 6:
                print("---------")
        print("__________________________________")


def solve_puzzle(initial_state):
    if not initial_state.is_solvable():
        return None
    visited = set()
    q = Queue()
    q.put((initial_state, []))

    while not q.empty():
        current_puzzle, path = q.get()
        if current_puzzle.is_solved():
            return path

        visited.add(current_puzzle.state)
        for direction in current_puzzle.directions:
            next_puzzle = current_puzzle.move_empty(direction)
            if next_puzzle and next_puzzle.state not in visited:
                q.put((next_puzzle, path + [next_puzzle]))

    return None


# 示例初始状态
initial = Puzzle("2831467 5")

# 检查是否可解并求解
if initial.is_solvable():
    solution_path = solve_puzzle(initial)
    if solution_path:
        for step in solution_path:
            step.print_puzzle()
    else:
        print("没有找到解决方案")
else:
    print("这个九宫格问题无解")
