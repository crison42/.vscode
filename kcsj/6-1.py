import re
import string


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
frequency_table = build_frequency_table(words)

word_to_search = input("请输入要检索的单词: ")
frequency, comparisons = sequential_search(frequency_table, word_to_search)

print(f"单词 '{word_to_search}' 在文章中出现 {frequency} 次.")

def calculate_asl(search_function, data_structure, data):
    total_comparisons = 0
    for item in data:
        _, comparisons = search_function(data_structure, item)
        total_comparisons += comparisons
    return total_comparisons / len(data)
# 计算平均查找长度
asl = calculate_asl(sequential_search, frequency_table, words)
print(f"平均查找长度 ASL= {asl}")