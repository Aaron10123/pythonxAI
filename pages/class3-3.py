import streamlit as st
import time

if "meals" not in st.session_state:  # 如果session_state中沒有meals
    st.session_state.meals = []  # 就建立一個meals=[]
st.title("點餐機")
col1, col2 = st.columns([5, 1])
with col1:
    text = st.text_input("請輸入餐點")
with col2:
    if st.button("加入"):
        if "text" not in st.session_state.meals:  # 如果session_state中沒有text
            st.session_state.meals.append(text)  # 將text加入list
        st.rerun()  # 重新執行頁面

st.markdown("---")  # 分隔線
st.title("購物車")

for index in range(len(st.session_state.meals)):  # 從0開始，到購物車中的元素數量
    cart1, cart2 = st.columns([5, 1])
    with cart1:
        st.markdown(f"{st.session_state.meals[index]}")  # 在第一欄建立使用者輸入的餐點
    with cart2:
        if st.button(f"刪除{st.session_state.meals[index]}", key=f"btn{index}"):
            st.session_state.meals.remove(
                st.session_state.meals[index]
            )  # 從list刪除該餐點
            # st.session_state.meals.pop(index)  # 從list刪除該餐點
            st.rerun()

if st.button("重新執行", key="btn"):
    st.success("重新執行")
    time.sleep(1)
    st.rerun()
