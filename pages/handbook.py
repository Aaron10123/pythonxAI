import streamlit as st
import os

folderpath = (
    "markdown"  # 這是相對路徑,C:\Users\USER\Desktop\pythonxAI\markdown這是絕對路徑
)

files = os.listdir(folderpath)  # 列出所有檔案
print(files)  # 印出所有檔案
files_name = []  # 新增一個空的list
for f in files:
    if f.endswith(".md"):  # 判斷檔案名稱是否為.md結尾
        files_name.append(f)  # 如果是就加入list
print(files_name)  # 印出所有檔案名稱

for f in files_name:  # 逐一讀取檔案名稱
    with open(
        f"{folderpath}/{f}", "r", encoding="utf-8"
    ) as file:  # (folderpath/檔案名稱,"r"=讀檔,編碼)
        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 建立一個擴展元件，標題為檔案名稱
        st.markdown(content)  # 印出檔案內容在擴展元件中
