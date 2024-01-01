def build_frequency_table(words):
    frequency_table = {}
    for word in words:
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1
    return frequency_table

def sequential_search(frequency_table, target_word):
    comparisons = 0
    for word, frequency in frequency_table.items():
        comparisons += 1
        if word == target_word:
            return frequency, comparisons
    return 0, comparisons  # 如果单词不在表中，返回词频0和比较次数

# 假设我们有一段文本
text = "This is a simple example text with several words with different frequencies"

# 简单的预处理：转为小写并分割成单词列表
words = text.lower().split()

# 构建频率表
frequency_table = build_frequency_table(words)

# 假设我们要查找单词 'with' 的词频
word_to_search = 'with'
frequency, comparisons = sequential_search(frequency_table, word_to_search)

print(f"Word '{word_to_search}' found with frequency {frequency} after {comparisons} comparisons.")

def calculate_asl(search_function, data_structure, data):
    total_comparisons = 0
    for item in data:
        _, comparisons = search_function(data_structure, item)
        total_comparisons += comparisons
    return total_comparisons / len(data)
# 计算平均查找长度
average_asl = calculate_asl(sequential_search, frequency_table, words)
print(f"Average ASL: {average_asl}")