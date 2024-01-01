import re
import string


class HashTableNode:
    def __init__(self, key, value=1):
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, size=1024):
        self.table = [None] * size
        self.size = size
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key):
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = HashTableNode(key)
        else:
            while True:
                if node.key == key:
                    node.value += 1
                    return
                if node.next is None:
                    break
                node = node.next
            node.next = HashTableNode(key)
    
    def search(self, key):
        index = self.hash(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None
    
        # 新增计算ASL的方法
    def calculate_asl(self):
        total_search_steps = 0
        total_elements = 0
        for node in self.table:
            while node:
                total_search_steps += self.search_steps(node.key)
                total_elements += 1
                node = node.next
        return total_search_steps / total_elements if total_elements else 0

    # 新增辅助方法，用于计算查找特定键所需的步数
    def search_steps(self, key):
        index = self.hash(key)
        node = self.table[index]
        steps = 1  # 开始搜索时步数为1
        while node:
            if node.key == key:
                return steps
            steps += 1
            node = node.next
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

words = read_and_clean_file('input.txt')
# 创建链地址法哈希表并插入单词
chaining_hash = ChainingHashTable(size=128)  # 假设我们设置哈希表大小为128
for word in words:
    chaining_hash.insert(word)

# 检索单词 'example' 的频率
frequency = chaining_hash.search('example')
print(f"Word 'example' occurs {frequency} times in the Chaining Hash Table.")

asl = chaining_hash.calculate_asl()
print(f"Average Search Length (ASL) for the Chaining Hash Table is: {asl}")