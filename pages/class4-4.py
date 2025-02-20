import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾下所有檔案名稱
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=50)
# 使用者輸入圖片大小,最小值為50,最大值為500,預設為100,每次增加50

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)
    # 顯示圖片,根據用戶輸入的圖片大小,可以調整圖片大小

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片,使用欄寬度
