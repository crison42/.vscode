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
    
# 使用之前提供的文本和预处理方法
text = "This is a simple example text with several words with different frequencies"
words = text.lower().split()

# 构建链表
linked_list = LinkedList()
for word in words:
    linked_list.insert(word)

# 查找单词 'with' 的词频
word_to_search = 'with'
frequency, comparisons = linked_list.search(word_to_search)

print(f"Word '{word_to_search}' found with frequency {frequency} after {comparisons} comparisons.")

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
print(f"Average Search Length (ASL) for linked list sequential search: {asl}")