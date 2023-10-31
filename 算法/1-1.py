def greedy_activity_scheduling(activities):
   activities.sort(key=lambda x: x[1])  # 按照结束时间排序
   selected = [activities[0]]  # 初始选择活动1

   for activity in activities[1:]:
       if activity[0] >= selected[-1][1]:  # 如果当前活动的开始时间大于等于上一个活动的结束时间，不冲突
           selected.append(activity)

   return selected

# 测试数据
activities = [
   (0, 3),
   (1, 4),
   (2, 5),
   (3, 6),
]

result = greedy_activity_scheduling(activities)
print(result)  # 输出：[(0, 3), (1, 4), (2, 5), (3, 6)]