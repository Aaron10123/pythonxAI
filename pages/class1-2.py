import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)

st.markdown(
    """
### Python 程式技巧筆記

#### 基本輸出與註解

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

#### 資料型別與基本輸出

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

#### 變數宣告與運算

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

#### 符號的優先順序

1. 括號 `()`
2. 指數 `**`
3. 乘、除、整除、取餘數 `* / // %`
4. 加、減 `+ -`

#### 字串運算

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

#### 型別轉換

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

#### 使用者輸入

- **基本輸入：**
  ```python
  a = input("請輸入一個數字:")
  print(f"input()輸入的內容是{a}")  # 印出輸入的內容
  print(f"input()輸入的內容型態是{type(a)}")  # 印出輸入的內容型態
  ```

#### 計算正方形的面積

- **計算與輸出：**
  ```python
  a = int(input("請輸入正方形的邊長:"))
  print(f"正方形的面積是{a*a}")  # 印出正方形的面積

  a = int(input("請輸入正方形的邊長:"))
  area = a**2
  print(f"正方形的面積是{area}")  # 印出正方形的面積
  ```

#### 其他快捷鍵提示

- **註解整行：**
  - 使用 `Ctrl + ?`
- **批次修改相同的地方：**
  - 使用 `Ctrl + F2`

這些筆記涵蓋了變數宣告、基本運算、資料型別、字串操作與格式化、型別轉換、基本輸入輸出等Python的基本技巧。希望對你有幫助！
"""
)
