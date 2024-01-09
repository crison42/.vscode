from collections import deque

# 定义获取移动后位置的函数
def get_new_position(zero_pos, move):
   moves = {
       'U': (-1, 0),
       'D': (1, 0),
       'L': (0, -1),
       'R': (0, 1)
   }
   return zero_pos[0] + moves[move][0], zero_pos[1] + moves[move][1]

# 定义检查位置是否有效的函数
def is_valid_position(pos):
   return 0 <= pos[0] < 3 and 0 <= pos[1] < 3

# 定义交换两个位置的函数
def swap(state, pos1, pos2):
   state = list(state)
   state[pos1], state[pos2] = state[pos2], state[pos1]
   return ''.join(state)

# 定义广度优先搜索函数
def bfs(start, goal):
   if start == goal:
       return ''
   queue = deque([(start, '', (-1, -1))])  # (state, path, zero_position)
   visited = {start}
   while queue:
       current_state, path, zero_pos = queue.popleft()
       
       if zero_pos == (-1, -1):
           zero_pos = current_state.index('0')
           zero_pos = (zero_pos // 3, zero_pos % 3)
       
       if current_state == goal:
           return path
       
       for move in ['U', 'D', 'L', 'R']:
           new_zero_pos = get_new_position(zero_pos, move)
           if is_valid_position(new_zero_pos):
               new_state = swap(current_state, zero_pos[0] * 3 + zero_pos[1], new_zero_pos[0] * 3 + new_zero_pos[1])
               if new_state not in visited:
                   queue.append((new_state, path + move, new_zero_pos))
                   visited.add(new_state)
   return "无解"

# 主函数
def main(input_string):
   start_state = input_string.replace(' ', '0')
   goal_state = "123456780"  # 目标状态
   result = bfs(start_state, goal_state)
   if result != "无解":
       print("找到解决方案，共移动{}步：{}".format(len(result), result))
   else:
       print(result)

# 输入数据
input_string = "2 3541687"  # 示例输入，你可以在这里随意更改
# 以下是示例输入的表格形式：
# —————————————
# | 2 | 0 | 3 |
# | 5 | 4 | 1 |
# | 6 | 8 | 7 |
# ——————————————
# 注意：0 代表空白位置，数字代表对应位置的数字。
main(input_string)