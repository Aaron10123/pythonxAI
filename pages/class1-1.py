# 可以在一行寫出多個語句
print("Hello World!")  # 這是印出Hello World!的程式碼


# 注意到循環的時候，可以在循環中印出其他語句
# for i in range(10):  # 循環10次
#     print(i)  # 這是印出i的值
# ctrl+F2 可跟改相同的地方
# ctrl+? 可註解一行
"""
可註解多行

"""

print(123)  # 整數
print(123.456)  # 浮點數
print(True)  # 布林值
print(False)  # 布林值
print("Hello World!")  # 字串
print('"')  # 印出雙引號
print("'")  # 印出單引號


a = 10  # 宣告變數-將10寫入變數a
print(a)  # 印出變數a的值
b = "Hello World!"  # 宣告變數-將Hello World!寫入變數b
print(b)  # 印出變數b的值

print(1 + 1)  # 加法計算
print(1 - 1)  # 減法計算
print(2 * 3)  # 乘法計算
print(10 / 3)  # 除法計算
print(10 // 3)  # 取整除法計算
print(10 % 3)  # 取餘數計算
print(2**3)  # 指數計算就是2的3次方

# 符號的優先順序
# 1.()
# 2.**
# 3.* / // %
# 4.+ -

# 字串運算
a = "Hello"
b = "World!"
print(a + b)  # 字串加法
print(a + " " + b)  # 字串加法
print(a * 3)  # 字串乘法
print(a + " " + b * 3)  # 字串加法乘法混合

print(f"Hello {10} World!")  # 字串格式化
# 在字串前加f可以在字串中加入變數,但要用{}括起來

print(len("Hello World!"))  # 字串長度
print(int("123"))  # 字串轉整數
print(float("123.456"))  # 字串轉浮點數
print(str(123))  # 整數轉字串
print(bool("True"))  # 字串轉布林值
print(bool("False"))  # 字串轉布林值
print(bool("Hello World!"))  # 字串轉布林值
print(bool(""))  # 字串轉布林值
print(bool("0"))  # 字串轉布林值
print(bool("123"))  # 字串轉布林值

print("input()可以在終端機輸入一個數字")  # 輸入一個數字
a = input("請輸入一個數字:")  # 讓用戶輸入一個數字且不會將文字存進變數
print(f"input()輸入的內容是{a}")  # 印出輸入的內容
print(f"input()輸入的內容型態是{type(a)}")  # 印出輸入的內容型態

# 計算正方形的面積
a = int(input("請輸入正方形的邊長:"))
print(f"正方形的面積是{a*a}")  # 印出正方形的面積

a = int(input("請輸入正方形的邊長:"))
area = a**2
print(f"正方形的面積是{area}")  # 印出正方形的面積
