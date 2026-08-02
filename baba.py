import streamlit as st
import datetime
import os
import base64

# Page Configuration
st.set_page_config(
    page_title="Baba's Special Corner",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------------------------------------------------------
# 🛠️ HELPER FUNCTIONS (IMAGE FINDER & BASE64 CONVERTER)
# -----------------------------------------------------------------------------

def find_image_path(base_name):
    """
    Check karega ke image jpg, JPG, png, ya jpeg me se kisi bhi naam se exist karti hai ya nahi.
    """
    extensions = ['.jpg', '.JPG', '.png', '.PNG', '.jpeg', '.JPEG']
    for ext in extensions:
        full_path = os.path.join("images", f"{base_name}{ext}")
        if os.path.exists(full_path):
            return full_path
    return None

def get_image_base64(image_path):
    """Local image ko base64 CSS background ke liye convert karta hai."""
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# -----------------------------------------------------------------------------
# 🖼️ BACKGROUND IMAGE SETUP (pic1)
# -----------------------------------------------------------------------------

bg_img_path = find_image_path("pic1")
bg_base64 = get_image_base64(bg_img_path)

if bg_base64:
    bg_css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)), 
                    url("data:image/jpeg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Custom Styling for Cards and Buttons
st.markdown("""
    <style>
    .heart-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
        margin-bottom: 25px;
        text-align: center;
    }
    .poetry-text {
        font-size: 20px;
        color: #1B5E20;
        font-weight: bold;
        line-height: 1.8;
    }
    .stButton>button {
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 12px 28px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 🌟 APP HEADER
# -----------------------------------------------------------------------------

st.title("❤️ Assalam-o-Alaikum Baba!")
st.caption(f"📅 Aaj Ki Tareekh: {datetime.date.today().strftime('%B %d, %Y')}")
st.write("---")

# -----------------------------------------------------------------------------
# 📸 SECTION 1: 5 PHOTOS SLIDER (SAFE LOADING)
# -----------------------------------------------------------------------------

st.subheader("🖼️ Humari Pyari Yaadein (5 Special Photos)")

captions = [
    "1. Aapke Saath Har Lamha Khaas Hai ❤️",
    "2. Baba — Mere Sar Ka Saaya 👑",
    "3. Aapki Smile Meri Sabse Badi Daulat 😊",
    "4. Purani Khubsurat Yaadein 📸",
    "5. Hamesha Aise Hi Muskurate Rahein! 🤲"
]

# Slider for selecting photos 1 to 5
selected_num = st.slider("Photo Badalne Ke Liye Slider Move Karein:", 1, 5, 1)

# Dynamic Image path finder
img_key = f"pic{selected_num}"
img_path = find_image_path(img_key)

if img_path:
    st.image(img_path, caption=captions[selected_num - 1], use_container_width=True)
else:
    st.error(f"⚠️ Image 'images/pic{selected_num}' nahi mili! Please check karein ke photo 'images' folder me exist karti hai ya nahi.")

st.write("---")

# -----------------------------------------------------------------------------
# 📜 SECTION 2: MUHABBAT BHARI LINES
# -----------------------------------------------------------------------------

st.markdown("""
    <div class="heart-card">
        <p class="poetry-text">
            "Suno Baba!<br>
            Aapka haath pakad kar chalna sikha hai,<br>
            Aapki chhaon mein hi mera har din khila hai.<br>
            Duniya ki har daulat ek taraf,<br>
            Aur aapki smile mere liye sabse bada in'aam hai!" ❤️
        </p>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 🤗 SECTION 3: MAGIC BUTTON & GREETING
# -----------------------------------------------------------------------------

current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greeting = "Subah Bakhair Baba! ☀️ Aaj ki chai pi li aapne?"
elif 12 <= current_hour < 17:
    greeting = "Dopahar Bakhair Baba! 🌤️ Khana waqt par kha lijiyega."
elif 17 <= current_hour < 21:
    greeting = "Shaam Bakhair Baba! ☕ Aaj shaam saath baithte hain!"
else:
    greeting = "Shab Bakhair Baba! 🌙 Sukoon ki neend soyein, main hu na!"

st.info(f"💡 **Aaj Ka Paigham:** {greeting}")

st.write("---")
st.subheader("🤗 Baba, Meri Yaad Aaye Toh Yahan Click Karein")

love_messages = [
    "Baba! Main aapko har pal yaad karta hu. Aap mere sabse bade hero hain! ❤️",
    "Aapne mere liye jitni mehnat ki hai, main unka karz kabhi ada nahi kar sakta. Allah aapko hamesha salamat rakhe! 🤲",
    "Jab bhi pareshan hon, yaad rakhiyega aapka beta/beti hamesha aapke saath khada hai! 🤝",
    "Aapki khushi meri sabse badi kamyabi hai. Hamesha aise hi muskurate rahein! 😊",
    "Chai ka waqt ho toh bataiye, saath baith kar purani baatein karte hain! ☕"
]

if st.button("❤️ Meri Awaaz / Message Sunen"):
    st.balloons()
    selected_msg = love_messages[datetime.datetime.now().second % len(love_messages)]
    st.success(f"**Baba Ke Liye Message:** {selected_msg}")

st.write("---")
st.caption("Aapka Pyara Beta/Beti | Made with ❤️ for My Beloved Father")
