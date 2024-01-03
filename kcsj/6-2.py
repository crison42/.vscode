import re
import string

class ListNode:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
        self.next = None  # 指向下一个节点

class LinkedList:
    def __init__(self):
        self.head = None  # 链表头部初始化为空

    def insert(self, word):
        # 如果单词已经在链表中，增加它的频率
        current = self.head
        while current is not None:
            if current.word == word:
                current.frequency += 1
                return
            current = current.next
        # 如果单词不在链表中，插入一个新节点到链表头部
        new_node = ListNode(word, 1)
        new_node.next = self.head
        self.head = new_node

    def search(self, target_word):
        current = self.head
        comparisons = 0
        while current is not None:
            comparisons += 1
            if current.word == target_word:
                return current.frequency, comparisons
            current = current.next
        return 0, comparisons  # 如果单词不在链表中，返回词频0和比较次数

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

# 构建链表
linked_list = LinkedList()
for word in words:
    linked_list.insert(word)

word_to_search = input("请输入要检索的单词: ")
frequency, comparisons = linked_list.search(word_to_search)

print(f"单词 '{word_to_search}' 在文章中出现 {frequency} 次.")

def calculate_asl_linked_list(linked_list):
    total_comparisons = 0
    total_elements = 0
    current = linked_list.head
    
    while current is not None:
        _, comparisons = linked_list.search(current.word)
        total_comparisons += comparisons
        total_elements += 1
        current = current.next
        
    asl = total_comparisons / total_elements if total_elements > 0 else 0
    return asl

# 计算链表的 ASL
asl = calculate_asl_linked_list(linked_list)
print(f"平均查找长度 ASL= {asl}")