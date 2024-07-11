i = 0
while i < 10:  # 當i小於10時，變一直執行直到i等於10
    print(i)
    i += 1

a = 10
a += 1  # a=a+1
print(a)
a -= 1  # a=a-1
print(a)
a /= 2  # a=a/2
print(a)
a //= 2  # a=a//2
print(a)
a %= 2  # a=a%2
print(a)
a *= 2  # a=a*2
print(a)
a **= 2  # a=a**2
print(a)


# 符號的優先順序
# 1.()
# 2.**
# 3.* / // %
# 4.+ -
# 5.< <= > >= == !=
# 6.and、or、not
# 7.= += -= *= /= //= %= **=

# 用break離開迴圈
i = 1
while i < 10:  # 當i小於10時，變一直執行直到i等於10
    if i == 5:  # 判斷是否等於5
        break  # 強制離開while迴圈
    print(i)
    i += 1
for i in range(10):  # 當i小於10時，變一直執行直到i等於10
    print(i)
    if i == 5:  # 判斷是否等於5
        break  # 強制離開for迴圈
# randoom
import random  # 匯入random模組

random.randrange(3)  # 隨機產生0到2的整數
random.randrange(1, 10)  # 隨機產生1到9的整數
random.randint(1, 10, 2)  # 隨機產生1到9的奇數
# radomrange跟range一樣，第一個數字是開始，第二個數字是結束，第三個數字是間隔
# 不會蜀道最後一個數字

random.randint(1, 10)  # 隨機產生1到10的整數
# randint跟range一樣，第一個數字是開始，第二個數字是結束
# 但randint一定要設定兩個數字，且會蜀道最後一個數字
