import re
import string

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

# 读取文件并清理标点
def read_and_clean_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # 使用正则表达式去除标点
        text = re.sub(r'[{}]+'.format(string.punctuation), ' ', text)
        # 分割单词并转换为小写
        words = text.lower().split()
    return words

words = read_and_clean_file('input.txt')

# 构建频率表
frequency_table = build_frequency_table(words)  # 使用之前给出的函数

# 为了进行折半查找，我们需要一个根据单词排序的顺序表
sorted_table = list(frequency_table.items())
sorted_table.sort(key=lambda item: item[0])

# 现在进行折半查找
word_to_search = input("请输入要检索的单词: ")
frequency, comparisons = binary_search(sorted_table, word_to_search)

print(f"单词 '{word_to_search}' 在文章中出现 {frequency} 次.")

def calculate_asl(search_function, data_structure, data):
    total_comparisons = 0
    for item in data:
        _, comparisons = search_function(data_structure, item)
        total_comparisons += comparisons
    return total_comparisons / len(data)
# 计算折半查找的平均ASL
asl = calculate_asl(binary_search, sorted_table, words)
print(f"平均查找长度 ASL= {asl}")