import re
import string

class OpenAddressingHashTable:
    def __init__(self, size=1024):
        self.table = [None] * size
        self.size = size
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key):
        index = self.hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index][1] += 1
                return
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full")
        self.table[index] = [key, 1]
    
    def search(self, key):
        index = self.hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return None
    # 计算ASL的方法
    def calculate_asl(self):
        total_search_steps = 0
        total_elements = 0
        for key, _ in filter(None, self.table):  # 过滤出所有非None的键值对
            total_search_steps += self.search_steps(key)
            total_elements += 1
        return total_search_steps / total_elements if total_elements else 0

    # 辅助方法，用于计算查找特定键所需的步数
    def search_steps(self, key):
        index = self.hash(key)
        start_index = index
        steps = 1  # 开始搜索时步数为1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return steps
            index = (index + 1) % self.size
            if index == start_index:
                return steps
            steps += 1
        return steps
    
# 读取文件并清理标点
def read_and_clean_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # 使用正则表达式去除标点
        text = re.sub(r'[{}]+'.format(string.punctuation), ' ', text)
        # 分割单词并转换为小写
        words = text.lower().split()
    return words
# 读取文件并统计单词频率
file_path = 'input.txt' 
words = read_and_clean_file(file_path)
# 创建开放地址法哈希表并插入单词
oahash = OpenAddressingHashTable(size=128)  # 假设设置哈希表大小为128
for word in words:
    oahash.insert(word)

word_to_search = input("请输入要检索的单词: ")
frequency = oahash.search(word_to_search)
print(f"单词 {word_to_search} 在文章中出现 {frequency} 次.")

asl= oahash.calculate_asl()
print(f"平均查找长度 ASL= {asl}")

