# 將元素增加到列表最後面
l = [1, 2, 3]
l.append(4)
print(l)

# 移除元素
l = [1, 2, 3, 1]
l.remove(1)
print(l)

# # 列表反轉
# l = [1, 2, 3]
# l.reverse()
# print(l)


# 計算特定元素的數量
l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))
# 回傳2

l = [9, 1, -4, 3, 7, 11, 3]
c = l.count(3)  # 計算l中有多少個3
for i in range(c):  # 把3們刪除
    l.remove(3)
    print(l)

# 移除最後一個元素
l = [9, 1, -4, 3, 7, 11, 3]
l.pop()
print(l)  # 移除3

# pop與remove的差異,pop適用index,remove是用元素來刪除

# 列表排序
l = [3, 1, 2]
l.sort()
print(l)
# 從小到大排序
l.sort(reverse=True)
print(l)
# 從大到小排序

l = [1, 2, 3, 1]
print(l.index(1))  # 找到1的位置
