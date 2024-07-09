# list的應用
[]  # 是一個空的list
[1, 2, 3]  # 是一個list，其中包含3個整數
["a", "b", "c"]  # 是一個list，其中包含3個字串
["a", 1, 2]  # 是一個list，其中包含3個字串和1個整數，可包含任何的值
# list裡面可以再加一個list

l = [1, 2, 3]  # 定義一個list
# 取值由0開始
l[0]  # 取第一個元素-回傳1
l[1]  # 取第二個元素-回傳2
l[2]  # 取第三個元素-回傳3

# 取長度
len([])  # 回傳0
len(["1"])  # 回傳1
len([1, 2])  # 回傳2
len([1, 2, 3])  # 回傳3

# 取值
l = ["a", "b", "c"]
for index in range(len(l)):
    print(l[index])  # 回傳a,b,c

# 依序取值
l = ["a", "b", "c"]
for element in l:
    print(element)  # 回傳a,b,c

# 設定值
l = ["a", "b", "c"]
l[0] = "d"  # 將第一個值設為d
print(l)  # 回傳['d','b','c']

# 刪除值
l = ["a", "b", "c"]
del l[0]
print(l)  # 回傳['b','c']
