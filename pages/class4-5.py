import streamlit as st
import os

st.title("購物平台")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾下所有檔案名稱
st.write(image_files)  # 顯示所有檔案的名稱
if "image" not in st.session_state:  # 如果session_state中沒有image
    st.session_state.image = []  # 就建立一個image=[]

row_quantity = st.number_input("欄數", min_value=2, value=1)
cols = st.columns(row_quantity)  # 分欄
for image_index in range(len(st.session_state.image)):  # 顯示所有圖片
    st.image(f"{image_folder}/{image_files[image_index]}", use_column_width=True)
    # 顯示圖片,使用欄寬度


st.title("新增商品庫存")
