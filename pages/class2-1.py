print(1 == 1)  # 這是比較是否相等的指令
print(1 != 1)  # 這是比較是否不相等的指令
print(1 < 1)  # 這是比較是否小於的指令
print(1 <= 1)  # 這是比較是否小於或等於的指令
print(1 > 1)  # 這是比較是否大於的指令
print(1 >= 1)  # 這是比較是否大於或等於的指令

print(not True)  # 這會顯示False-相反的運算
print(not False)  # 這會顯示True-相反的運算

print(False and True)  # 這會顯示False-要全部都符合條件才會顯示True
print(True and False)  # 這會顯示False-要全部都符合條件才會顯示True
print(False and False)  # 這會顯示False-要全部都符合條件才會顯示True
print(True and True)  # 這會顯示True-要全部都符合條件才會顯示True

print(False or True)  # 這會顯示True-只要有一個符合條件就會顯示True
print(True or False)  # 這會顯示True-只要有一個符合條件就會顯示True
print(False or False)  # 這會顯示False-只要有一個符合條件就會顯示True
print(True or True)  # 這會顯示True-只要有一個符合條件就會顯示True

# 符號的優先順序
# 1.()
# 2.**
# 3.* / // %
# 4.+ -
# 5.< <= > >= == !=
# 6.and、or、not

password = input("請輸入密碼:")
if password == "1234":
    print("歡迎光臨")
elif password == "5678":
    print("歡迎光臨")
else:
    print("密碼錯誤")
# 判斷一定要是if而不是elif、else，if只能有一個
# 判斷可以有無限個elif，也可以沒有
# 判斷只能有一個else，也可以沒有
# elif和else都是選擇性的

# 判斷是否是奇數
num = int(input("請輸入一個數字:"))
if num % 2 == 1:  # 判斷是否是奇數
    print(f"{num}是奇數")
else:  # 判斷是否是偶數
    print(f"{num}是偶數")
