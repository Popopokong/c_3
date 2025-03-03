import streamlit as st

# ตั้งค่าหน้าหลัก
st.set_page_config(page_title="Well Shop", layout="wide")

# URL หรือ path ของภาพโปรโมชั่น
promo_image = "https://i.imgur.com/r8bBx59.jpeg"
# สไตล์ CSS ที่ปรับปรุงใหม่
st.markdown(f"""
    <style>
        html, body, [class*="st-emotion-cache"] {{
            font-family: 'Arial', sans-serif;
            background-color: #a4e7a7;
        }}

        /* ชื่อร้าน */
        .title {{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }}

        /* แบนเนอร์ */
        .banner {{
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 3px 5px 15px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            position: relative;
            margin-bottom: 40px;
        }}

        /* รูปภาพโปรโมชั่น */
        .banner img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 20px;
            opacity: 0.85;
        }}

        /* ข้อความบนแบนเนอร์ */
        .banner-text {{
            position: absolute;
            font-size: 32px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        }}

        /* หัวข้อสินค้า */
        .subtitle {{
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: #444;
        }}

        /* กล่องสินค้า */
        .product-box {{
            width: 100%;
            border-radius: 15px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            text-align: center;
            background: white;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 20px;
        }}

        .product-box img {{
            width: 100%;
            height: 160px;
            object-fit: cover;
            border-radius: 10px;
        }}

        .product-box:hover {{
            transform: scale(1.05);
            box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.2);
        }}

        /* ชื่อสินค้า */
        .product-name {{
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }}

        /* ราคาสินค้า */
        .product-price {{
            font-size: 14px;
            color: #E44D26;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

# ชื่อร้าน
st.markdown("<div class='title'>Well Shop</div>", unsafe_allow_html=True)

# แบนเนอร์ พร้อมภาพโปรโมชั่น
st.markdown(f"""
    <div class='banner'>
        <img src='{promo_image}' alt='Promotion'>
        <div class='banner-text'>🔥 Special Promotion - Limited Time! 🔥</div>
    </div>
""", unsafe_allow_html=True)

# หัวข้อสินค้า
st.markdown("<div class='subtitle'>Our Products</div>", unsafe_allow_html=True)

# รายการสินค้า
products = [
    {"name": "Nike Sneakers", "price": "$120", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Luxury Watch", "price": "$250", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Leather Bag", "price": "$180", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Wireless Headphones", "price": "$90", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Stylish Sunglasses", "price": "$60", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Gaming Laptop", "price": "$1500", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Smartphone", "price": "$799", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Digital Camera", "price": "$550", "image": "https://i.imgur.com/r8bBx59.jpeg"},
    {"name": "Gaming Console", "price": "$499", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "Mechanical Keyboard", "price": "$120", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "Wireless Mouse", "price": "$40", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "4K Monitor", "price": "$350", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "Luxury Perfume", "price": "$75", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "Premium Coffee Beans", "price": "$25", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "Portable Speaker", "price": "$99", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
    {"name": "Mountain Bike", "price": "$800", "image": "https://i.imgur.com/v5fSGVg.jpeg"},
]

# แสดงสินค้าเป็นตาราง 4×4 พร้อมเพิ่มระยะห่าง
rows = 4
cols = 4
index = 0

for _ in range(rows):
    col_group = st.columns(cols)
    for col in col_group:
        if index < len(products):
            product = products[index]
            with col:
                st.markdown(f"""
                    <div class='product-box'>
                        <img src='{product["image"]}' alt='{product["name"]}'>
                        <div class='product-name'>{product["name"]}</div>
                        <div class='product-price'>{product["price"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            index += 1
