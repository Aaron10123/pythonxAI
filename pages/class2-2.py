import streamlit as st

number = st.number_input("請輸入一個數字", step=1)
# step=2表示每次輸入時數字的值會增加2
st.markdown(f"你輸入的數字是{number}")


# score = st.number_input("請輸入你的成績", min_value=0, max_value=100, step=1)
# if score < 60:
#     level = "F"
# elif score < 70 and score >= 60:
#     level = "D"
# elif score < 80 and score >= 70:
#     level = "C"
# elif score < 90 and score >= 80:
#     level = "B"
# else:
#     level = "A"
# st.markdown(f"你的等級是{level}")
st.title("分數練習")

score = st.number_input("請輸入你的成績", min_value=0, max_value=100, step=1)
if score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
elif score >= 60:
    level = "D"
else:
    level = "F"
st.markdown(f"你的等級是{level}")

st.title("按鈕練習")
st.button("點我", key="button")

if st.button("點我", key="button2"):
    st.balloons()

if st.button("點我", key="button3"):
    st.snow()
