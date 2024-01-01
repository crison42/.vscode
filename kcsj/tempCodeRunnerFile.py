def calculate_chaining_hash_asl(hash_table):
#     total_comparisons = 0
#     total_elements = 0
#     for i in range(hash_table.size):
#         chain = hash_table.table[i]
#         chain_length = len(chain)
#         for j in range(chain_length):
#             # 每个元素在链表中的位置决定了它的查找次数
#             total_comparisons += j + 1
#         total_elements += chain_length
#     return total_comparisons / total_elements if total_elements > 0 else 0
# # 计算平均查找长度
# asl = calculate_chaining_hash_asl(chaining_hash)
# print(f"The average search length (ASL) of the Chaining Hash Table is: {asl}")