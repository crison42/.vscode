def tsp(distances):
    N = len(distances)
    min_path = float('inf')
    path = []
    
    def backtrack(current_city, visited, current_length, local_path):
        nonlocal min_path, path
        if len(visited) == N:
            total_length = current_length + distances[current_city][0]  # 回到起点城市
            if total_length < min_path:
                min_path = total_length
                path = local_path + [0]  # 添加起点城市形成闭环
            return
        for next_city in range(N):
            if next_city not in visited:
                visited.add(next_city)
                backtrack(next_city, visited, current_length + distances[current_city][next_city], local_path + [next_city])
                visited.remove(next_city)
    
    backtrack(0, {0}, 0, [0])
    return min_path, path

# 城市间距离矩阵
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_path, path = tsp(distances)
print("Minimum path length:", min_path)
print("Path:", path)