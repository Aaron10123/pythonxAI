import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 建立2欄  col1和col2都是可以改變的變數，從左到右新增欄位
col1.button("按鈕1")  # 在第一欄建立按鈕
col2.button("按鈕2")  # 在第二欄建立按鈕

with col1:  # 在col1中建立任意的元件
    st.markdown("欄位1")
    st.button("左按鈕")
with col2:  # 在col2中建立任意的元件
    st.markdown("欄位2")
    st.button("右按鈕")

cols = st.columns(3)  # 建立3欄
cols[0].button("按鈕1", key="1")  # 在第一欄建立按鈕
cols[1].button("按鈕2", key="2")  # 在第二欄建立按鈕
cols[2].button("按鈕3", key="3")  # 在第三欄建立按鈕
# 將欄位吋到同一個變數中，讓cols變成一個list
