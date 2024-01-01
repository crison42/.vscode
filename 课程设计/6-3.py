def binary_search(sorted_table, target_word):
    low = 0
    high = len(sorted_table) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        mid_word, mid_frequency = sorted_table[mid]

        if mid_word == target_word:
            return mid_frequency, comparisons
        elif mid_word < target_word:
            low = mid + 1
        else:
            high = mid - 1

    return 0, comparisons  # 如果单词不在顺序表中，返回词频0和比较次数

def build_frequency_table(words):
    frequency_table = {}
    for word in words:
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1
    return frequency_table

# 假设我们有一段文本
text = "This is a simple example text with several words with different frequencies"

# 简单的预处理：转为小写并分割成单词列表
words = text.lower().split()

# 构建频率表
frequency_table = build_frequency_table(words)  # 使用之前给出的函数

# 为了进行折半查找，我们需要一个根据单词排序的顺序表
sorted_table = list(frequency_table.items())
sorted_table.sort(key=lambda item: item[0])

# 现在进行折半查找
word_to_search = 'with'
frequency, comparisons = binary_search(sorted_table, word_to_search)

print(f"Word '{word_to_search}' found with frequency {frequency} after {comparisons} comparisons.")

def calculate_asl(search_function, data_structure, data):
    total_comparisons = 0
    for item in data:
        _, comparisons = search_function(data_structure, item)
        total_comparisons += comparisons
    return total_comparisons / len(data)
# 计算折半查找的平均ASL
average_asl = calculate_asl(binary_search, sorted_table, words)
print(f"Average ASL for binary search: {average_asl}")