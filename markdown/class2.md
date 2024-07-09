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
