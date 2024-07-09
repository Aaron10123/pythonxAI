import streamlit as st

with st.expander("class1 程式筆記"):
    st.markdown(
        """
    # Python程式技巧筆記

## 基本輸出與註解

- **單行輸出：**

  ```python
  print("Hello World!")  # 這是印出Hello World!的程式碼
  ```

- **多行註解：**

  ```python
  '''
  可註解多行
  '''
  ```

- **單行註解：**

  ```python
  # 這是單行註解
  ```

## 資料型別與基本輸出

- **整數、浮點數、布林值、字串的輸出：**

  ```python
  print(123)        # 整數
  print(123.456)    # 浮點數
  print(True)       # 布林值
  print(False)      # 布林值
  print("Hello World!")  # 字串
  print('"')        # 印出雙引號
  print("'")        # 印出單引號
  ```

## 變數宣告與運算

- **變數宣告與賦值：**

  ```python
  a = 10  # 宣告變數-將10寫入變數a
  print(a)  # 印出變數a的值
  b = "Hello World!"  # 宣告變數-將Hello World!寫入變數b
  print(b)  # 印出變數b的值
  ```

- **數學運算：**

  ```python
  print(1 + 1)    # 加法計算
  print(1 - 1)    # 減法計算
  print(2 * 3)    # 乘法計算
  print(10 / 3)   # 除法計算
  print(10 // 3)  # 取整除法計算
  print(10 % 3)   # 取餘數計算
  print(2**3)     # 指數計算（2的3次方）
  ```

## 符號的優先順序

1. 括號 `()`
2. 指數 `**`
3. 乘、除、整除、取餘數 `* / // %`
4. 加、減 `+ -`

## 字串運算

- **字串加法與乘法：**

  ```python
  a = "Hello"
  b = "World!"
  print(a + b)  # 字串加法
  print(a + " " + b)  # 字串加法
  print(a * 3)  # 字串乘法
  print(a + " " + b * 3)  # 字串加法乘法混合
  ```

- **字串格式化：**

  ```python
  print(f"Hello {10} World!")  # 字串格式化
  # 在字串前加f可以在字串中加入變數,但要用{}括起來
  ```

## 型別轉換

- **字串長度與型別轉換：**

  ```python
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
  ```

## 使用者輸入

- **基本輸入：**

  ```python
  a = input("請輸入一個數字:")
  print(f"input()輸入的內容是{a}")  # 印出輸入的內容
  print(f"input()輸入的內容型態是{type(a)}")  # 印出輸入的內容型態
  ```

## 計算正方形的面積

- **計算與輸出：**

  ```python
  a = int(input("請輸入正方形的邊長:"))
  print(f"正方形的面積是{a*a}")  # 印出正方形的面積

  a = int(input("請輸入正方形的邊長:"))
  area = a**2
  print(f"正方形的面積是{area}")  # 印出正方形的面積
  ```

## 其他快捷鍵提示

- **註解整行：**
  - 使用 `Ctrl + ?`
- **批次修改相同的地方：**
  - 使用 `Ctrl + F2`

## Streamlit 範例

這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：

- **粗體文字**
- *斜體文字*
- [連結](https://www.example.com)
- 代碼塊：

```python
print("Hello, Streamlit!")
```

    """
    )

with st.expander("class2 程式筆記"):
    st.markdown(
        """
    # 比較運算符

```python
print(1 == 1)  # 這是比較是否相等的指令
print(1 != 1)  # 這是比較是否不相等的指令
print(1 < 1)  # 這是比較是否小於的指令
print(1 <= 1)  # 這是比較是否小於或等於的指令
print(1 > 1)  # 這是比較是否大於的指令
print(1 >= 1)  # 這是比較是否大於或等於的指令
```

## 邏輯運算符

```python
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
```

### 符號的優先順序

1.()
2.**
3.* / // %
4.+ -
5.< <= > >= == !=
6.and、or、not

### 條件判斷

```python
password = input("請輸入密碼:")
if password == "1234":
    print("歡迎光臨")
elif password == "5678":
    print("歡迎光臨")
else:
    print("密碼錯誤")
```

### 判斷奇數或偶數

```python
num = int(input("請輸入一個數字:"))
if num % 2 == 1:  # 判斷是否是奇數
    print(f"{num}是奇數")
else:  # 判斷是否是偶數
    print(f"{num}是偶數")
```

### 使用 Streamlit 輸入數字

```python
import streamlit as st

number = st.number_input("請輸入一個數字", step=1)
st.markdown(f"你輸入的數字是{number}")
```

### 成績等級判斷

```python
import streamlit as st

st.title("分數練習")
score = st.number_input("請輸入你的成績", min_value=0, max_value=100, step=1)
if score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
elif score >= 60:
    level = "D"
else:
    level = "F"
st.markdown(f"你的等級是{level}")
```

### Streamlit 按鈕練習

```python
import streamlit as st

st.title("按鈕練習")
st.button("點我", key="button")

if st.button("點我", key="button2"):
    st.balloons()

if st.button("點我", key="button3"):
    st.snow()
```

### 迴圈

```python
for i in range(10):
    print(i)
# 這是一個迴圈，i是迴圈變數，它會從0開始，直到10

for i in range(2, 10):
    print(i)
# 這是一個迴圈，i是迴圈變數，它會從2開始，直到10

for i in range(10, 0, -1):
    print(i)
# 這是一個迴圈，i是迴圈變數，它會從10開始，直到0，每次反向計數

for i in range(0, 10, 2):
    print(i)
# 這是一個迴圈，i是迴圈變數，它會從0開始，直到10，每次計數2

for i in range(10, 2, -2):
    print(i)
# 這是一個迴圈，i是迴圈變數，它會從10開始，直到2，每次反向計數2
```

### Streamlit 數字金字塔

```python
import streamlit as st

st.title("數字金字塔")
i = st.number_input("請輸入一個整數(1~9)", min_value=1, max_value=9, step=1)
st.markdown("數字金字塔:")
for i in range(1, i + 1):
    st.markdown(str(i) * i)
```

### Streamlit 箭頭金字塔

```python
import streamlit as st

st.title("箭頭金字塔")
number = st.number_input("請輸入一個整數", step=1)
arrow = ""
for i in range(1, number * 2, 2):
    arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(1, number + 1):
    arrow += " " * (number - 1) + "*" + "\n"
st.markdown(f"```\n箭頭金字塔：\n{arrow}\n```")
```

    """
    )
