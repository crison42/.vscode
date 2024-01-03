import re
import string

class BSTNode:
    def __init__(self, key, value=1):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:  # key is in the tree, increment its value
            node.value += 1
        return node
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return node.value
        
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
# 创建二叉排序树并插入单词
bst = BinarySearchTree()
for word in words:
    bst.insert(word)

word_to_search = input("请输入要检索的单词: ")
frequency = bst.search(word_to_search)
print(f"单词 {word_to_search} 在文章中出现 {frequency} 次.")

def calculate_bst_asl(bst):
    def inorder_traverse(node, current_depth, results):
        if node is None:
            return
        # 左子树
        inorder_traverse(node.left, current_depth + 1, results)
        # 访问节点时记录深度（比较次数）
        results.append(current_depth)
        # 右子树
        inorder_traverse(node.right, current_depth + 1, results)
    
    depths = []
    inorder_traverse(bst.root, 1, depths)
    return sum(depths) / len(depths) if depths else 0
# 计算二叉搜索树平均查找长度
asl = calculate_bst_asl(bst)
print(f"平均查找长度 ASL= {asl}")
