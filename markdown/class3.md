# 程式技巧筆記

## 列表操作

### 將元素增加到列表最後面

使用 `append()` 方法將元素增加到列表的最後面。

```python
l = [1, 2, 3]
l.append(4)
print(l)  # 輸出: [1, 2, 3, 4]
```

### 移除元素

使用 `remove()` 方法移除列表中的第一個匹配的元素。

```python
l = [1, 2, 3, 1]
l.remove(1)
print(l)  # 輸出: [2, 3, 1]
```

### 計算特定元素的數量

使用 `count()` 方法計算列表中某個特定元素的數量。

```python
l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))  # 輸出: 2
```

### 刪除所有特定元素

利用 `count()` 方法計算元素數量，然後用 `remove()` 方法刪除所有出現的特定元素。

```python
l = [9, 1, -4, 3, 7, 11, 3]
c = l.count(3)  # 計算l中有多少個3
for i in range(c):  # 把3們刪除
    l.remove(3)
    print(l)
```

### 移除最後一個元素

使用 `pop()` 方法移除列表中的最後一個元素。

```python
l = [9, 1, -4, 3, 7, 11, 3]
l.pop()
print(l)  # 輸出: [9, 1, -4, 3, 7, 11]
```

### 列表排序

使用 `sort()` 方法對列表進行排序。

```python
l = [3, 1, 2]
l.sort()
print(l)  # 從小到大排序，輸出: [1, 2, 3]

l.sort(reverse=True)
print(l)  # 從大到小排序，輸出: [3, 2, 1]
```

### 找到特定元素的位置

使用 `index()` 方法找到元素在列表中的位置。

```python
l = [1, 2, 3, 1]
print(l.index(1))  # 輸出: 0
```

## Streamlit 操作

### 建立欄位和按鈕

使用 `columns()` 方法建立多欄布局，並在各欄中加入按鈕。

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 建立2欄
col1.button("按鈕1")  # 在第一欄建立按鈕
col2.button("按鈕2")  # 在第二欄建立按鈕

with col1:
    st.markdown("欄位1")
    st.button("左按鈕")
with col2:
    st.markdown("欄位2")
    st.button("右按鈕")

cols = st.columns([3, 3, 1])  # 建立3欄，改變欄位大小
cols[0].button("按鈕1", key="1")  # 在第一欄建立按鈕
cols[1].button("按鈕2", key="2")  # 在第二欄建立按鈕
cols[2].button("按鈕3", key="3")  # 在第三欄建立按鈕
```

### 文字輸入框

使用 `text_input()` 方法建立文字輸入元件。

```python
st.title("文字輸入框")
text = st.text_input("請輸入文字")
st.markdown(f"您輸入的文字是：{text}")
```

### session_state

使用 `session_state` 保存和更新狀態。

```python
if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("session_state按鈕", key="session_state_btn"):
    st.session_state.ans += 1
st.markdown(f"##### {st.session_state.ans}")
```

### 點餐機和購物車

使用 `session_state` 實現點餐機和購物車功能。

```python
if "meals" not in st.session_state:
    st.session_state.meals = []
st.title("點餐機")
col1, col2 = st.columns([5, 1])
with col1:
    text = st.text_input("請輸入餐點")
with col2:
    if st.button("加入"):
        if text not in st.session_state.meals:
            st.session_state.meals.append(text)
        st.rerun()

st.markdown("---")
st.title("購物車")

for index in range(len(st.session_state.meals)):
    cart1, cart2 = st.columns([5, 1])
    with cart1:
        st.markdown(f"{st.session_state.meals[index]}")
    with cart2:
        if st.button(f"刪除{st.session_state.meals[index]}", key=f"btn{index}"):
            st.session_state.meals.remove(st.session_state.meals[index])
            st.rerun()

if st.button("重新執行", key="btn"):
    st.success("重新執行")
    time.sleep(1)
    st.rerun()
```
