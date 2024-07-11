# 字典
{}  # 空字典
{
    "a": 1,
    "b": 2,
}  # 字典'a'和'b'為鍵(key)，1和2為值(value)，key可以是任意不可變的值，value可以是任意值
book = {"星期一": "蘋果", "星期二": "香蕉"}
print(book)  # {'星期一': '蘋果', '星期二': '香蕉'}
print(book["星期一"])  # 蘋果
# 鍵不可重複，值可重複，用冒號串聯，用逗號隔開

# 字典走訪
d = {"星期一": "蘋果", "星期二": "香蕉"}
for key in d:  # 如果直接將字典當作迴圈範圍的話，只會列出key，不會列出value
    print(key, d[key])

for key in d.keys():  # 可以使用keys()取得key
    print(
        key,
    )
# 以上兩種方法都可以取得key，結果相同

for value in d.values():  # 可以使用values()取得所有value
    print(value)

for key, value in d.items():  # 可以使用items()取得所有key和value
    print(key, value)

for key, value in d.items():  # 可以使用items()取得所有key和value
    print(f"key={key},value={value}")
for key, value in d.items():  # 可以使用items()取得所有key和value ，一起存到一個變數裡
    print(f"key={key},value={value}")
# 元素新增/修改
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "香蕉"
d["星期三"] = "蘋果"  # 新增元素,當key不存在時會新增元素
print(d)

# 檢查key是否存在
d = {"星期一": "蘋果", "星期二": "香蕉"}
print("星期一" in d)  # True
print("星期三" in d)  # False
# value有沒有存在
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True
# in可以用於字典和list，如果字典內容包含字串，就會回傳True
L = ["星期一", "星期二"]
print("星期一" in L)  # True
print("星期三" in L)  # False
# 刪除元素
d = {"星期一": "蘋果", "星期二": "香蕉"}
d.pop("星期一")  # 刪除星期一
print(d)
d.pop("星期三", "找不到")  # 如果星期三不存在，就會回傳找不到
print(d)
