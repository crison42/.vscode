# 活动安排问题的贪心算法


# 定义活动类，包含开始时间和结束时间
class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"({self.start}, {self.end})"


def greedy_activity_scheduling(activities):
    # 根据活动的结束时间进行排序
    activities.sort(key=lambda x: x.end)

    selected = []  # 存储选中的活动
    current = activities[0]  # 当前选择的活动
    for activity in activities[1:]:
        # 如果活动的开始时间在当前活动结束时间之后，表示不冲突，将其加入方案中
        if activity.start >= current.end:
            selected.append(current)
            current = activity

    selected.append(current)
    return selected


# 测试数据
activities = [
    Activity(1, 3),
    Activity(2, 5),
    Activity(4, 7),
    Activity(6, 9),
    Activity(8, 11),
]
selected_activities = greedy_activity_scheduling(activities)
for activity in selected_activities:
    print(activity)
