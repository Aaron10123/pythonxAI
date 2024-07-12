import streamlit as st
import time
import os

# 設計思路：
# 1.取得資料夾下所有圖片
# 2.建立product字典，字典中包含圖片名稱，價格，庫存，圖片
# 3.分欄顯示圖片

image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾下所有檔案名稱

if "products" not in st.session_state:  # 如果session_state中沒有product
    st.session_state.products = {}  # 就建立一個products字典

for image_file in image_files:  # 顯示所有圖片
    product_name = image_file[:-4]  # 去掉圖片名稱後的後四個字
    if (
        product_name not in st.session_state.products
    ):  # 如果product不存在，就建立一個product
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }  # 就建立一個product={}

# products範例
# products={"蘋果":{"price":10,"stock":10,"image":"image/蘋果.jpg"},
#         "香蕉":{"price":10,"stock":10,"image":"image/香蕉.jpg"},
#         "蔬菜":{"price":10,"stock":10,"image":"image/蔬菜.jpg"}}


# 顯示商品
st.title("購物平台")
col_num = st.number_input("欄數", min_value=1, value=2, step=1)
cols = st.columns(col_num)
i = 0
for product_name, details in st.session_state.products.items():
    with cols[i % col_num]:  # 透過取餘數來決定product在哪一列
        st.image(details["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格：{details['price']}")
        st.markdown(f"庫存：{details['stock']}")

        if st.button(f"購買{product_name}", key=f"{product_name}"):
            if details["stock"] > 0:  # 如果庫存大於0，就减庫存
                details["stock"] -= 1
                st.success(f"成功購買{product_name}")
                time.sleep(1)
                st.rerun()
            else:  # 如果庫存為0，就強制重新執行
                st.error(f"庫存為,無法購買{product_name}")

        i += 1

# 新增商品庫存功能
st.title("新增商品庫存")
product_name = list(st.session_state.products.keys())
col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", product_name)
with col2:
    new_stock = st.number_input("新增庫存", min_value=1, step=1)

if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += new_stock
    st.success(f"成功新增庫存")
    time.sleep(1)
    st.rerun()

# # 刪除商品庫存功能
# st.title("刪除商品庫存")
# product_name = list(st.session_state.products.keys())
# col1, col2 = st.columns(2)
# with col1:
#     selected_product = st.selectbox("選擇商品", product_name)
# with col2:
#     new_stock = st.number_input("刪除庫存", min_value=1, step=1)

# if st.button("刪除庫存"):
#     st.session_state.products[selected_product]["stock"] -= new_stock
#     st.success(f"成功刪除庫存")
#     time.sleep(1)
#     st.rerun()

# 重新顯示商品庫存
st.markdown("目前商品庫存")
for product_name, details in st.session_state.products.items():
    st.markdown(f"{product_name}:{details['stock']}件")
