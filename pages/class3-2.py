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

cols = st.columns([3, 3, 1])  # 建立3欄 ，用list(3比3比1)改變欄位大小
cols[0].button("按鈕1", key="1")  # 在第一欄建立按鈕
cols[1].button("按鈕2", key="2")  # 在第二欄建立按鈕
cols[2].button("按鈕3", key="3")  # 在第三欄建立按鈕
# 將欄位吋到同一個變數中，讓cols變成一個list

st.title("文字輸入框")
text = st.text_input("請輸入文字")  # 建立文字輸入元件
st.markdown(f"您輸入的文字是：{text}")

st.title("sesssion_state")
ans = 1
st.write(f"##### {ans}")
if st.button(
    "按鈕", key="btn"
):  # 如果按鈕被按下，頁面會重新執行，這個城市同時抱括建立以及偵測是否被按下
    ans += 1  # ans=ans+1
st.markdown(f"##### {ans}")  # 這時候ans會是2，不會變成3，因為頁面會重新執行
# 上面的是錯的

if "ans" not in st.session_state:  # 如果session_state中沒有ans
    st.session_state.ans = 1  # 就建立一個ans=1

if st.button(
    "session_state按鈕", key="session_state_btn"
):  # 如果按鈕被按下，頁面會重新執行
    st.session_state.ans += 1  # session_state中的ans加1，這時候ans可以持續增加
st.markdown(f"##### {st.session_state.ans}")
