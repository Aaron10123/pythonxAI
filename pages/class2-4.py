import streamlit as st

st.title("數字金字塔")
i = st.number_input("請輸入一個整數(1~9)", min_value=1, max_value=9, step=1)
st.markdown("數字金字塔:")
for i in range(1, i + 1):
    st.markdown(str(i) * i)


# x = int(input("請輸入要印出的箭頭大小"))
# y = -1
# z = x
# for i in range(x):
#     z -= 1
#     y += 2
#     val = " " * z + "*" * y
#     print(val)
# x -= 1
# for z in range(x + 1):
#     a = " " * x + "*" * 1
#     print(a)

st.title("箭頭金字塔")
# number = int(input("請輸入一個整數"))
number = st.number_input("請輸入一個整數", step=1)
arrow = ""
for i in range(1, number * 2, 2):
    # print(" " * ((number * 2 - i) // 2) + "*" * i)
    arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(1, number + 1):
    # print(" " * (number - 1) + "*")
    arrow += " " * (number - 1) + "*" + "\n"
st.markdown(
    f"""
    ```\n 箭頭金字塔：\n{arrow}\n```
"""
)
