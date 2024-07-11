# 程式技巧筆記

## While 迴圈

```python
i = 0
while i < 10:  # 當 i 小於 10 時，會一直執行直到 i 等於 10
    print(i)
    i += 1
```

## 複合運算符號

```python
a = 10
a += 1  # 等同於 a = a + 1
print(a)
a -= 1  # 等同於 a = a - 1
print(a)
a /= 2  # 等同於 a = a / 2
print(a)
a //= 2  # 等同於 a = a // 2
print(a)
a %= 2  # 等同於 a = a % 2
print(a)
a *= 2  # 等同於 a = a * 2
print(a)
a **= 2  # 等同於 a = a ** 2
print(a)
```

## 符號的優先順序

1. `()`
2. `**`
3. `* / // %`
4. `+ -`
5. `< <= > >= == !=`
6. `and、or、not`
7. `= += -= *= /= //= %= **=`

## 使用 `break` 離開迴圈

```python
i = 1
while i < 10:  # 當 i 小於 10 時，會一直執行直到 i 等於 10
    if i == 5:  # 判斷是否等於 5
        break  # 強制離開 while 迴圈
    print(i)
    i += 1

for i in range(10):  # 當 i 小於 10 時，會一直執行直到 i 等於 10
    print(i)
    if i == 5:  # 判斷是否等於 5
        break  # 強制離開 for 迴圈
```

## 使用 `random` 模組

```python
import random  # 匯入 random 模組

random.randrange(3)  # 隨機產生 0 到 2 的整數
random.randrange(1, 10)  # 隨機產生 1 到 9 的整數
random.randint(1, 10)  # 隨機產生 1 到 10 的整數
```

## 隨機數字猜測遊戲

```python
import random

a = random.randint(1, 100)

while True:
    answer = int(input("Enter a number between 1 and 100: "))
    if answer == a:
        print("You win!")
        break
    elif answer < a:
        print("more")
    elif answer > a:
        print("smaller")
    else:
        print("Invalid number")
```

## 字典

### 創建與使用

```python
book = {"星期一": "蘋果", "星期二": "香蕉"}
print(book)  # {'星期一': '蘋果', '星期二': '香蕉'}
print(book["星期一"])  # 蘋果
```

### 走訪字典

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
for key in d:  # 列出所有的 key
    print(key, d[key])

for key in d.keys():  # 使用 keys() 取得 key
    print(key)

for value in d.values():  # 使用 values() 取得所有 value
    print(value)

for key, value in d.items():  # 使用 items() 取得所有 key 和 value
    print(f"key={key},value={value}")
```

### 元素新增/修改

```python
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "香蕉"
d["星期三"] = "蘋果"  # 當 key 不存在時會新增元素
print(d)
