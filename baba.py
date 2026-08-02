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
# 🖼️ LOCAL IMAGES LOADING & BACKGROUND SETUP
# -----------------------------------------------------------------------------
# Function to convert local image to base64 for CSS background
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Background ke liye pehli photo (pic1.jpg) use kar rahe hain
bg_image_path = "images/pic1.jpg"
bg_base64 = get_image_base64(bg_image_path)

# Custom CSS for Background and Card Styling
bg_css = f"""
<style>
.stApp {{
    background: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)), 
                url("data:image/jpg;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.heart-card {{
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
    margin-bottom: 25px;
    text-align: center;
}}

.poetry-text {{
    font-size: 20px;
    color: #1B5E20;
    font-weight: bold;
    line-height: 1.8;
}}

.stButton>button {{
    background-color: #2E7D32 !important;
    color: white !important;
    border-radius: 25px !important;
    padding: 12px 28px !important;
    font-weight: bold !important;
    border: none !important;
}}
</style>
"""
st.markdown(bg_css, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 🌟 APP CONTENT
# -----------------------------------------------------------------------------

st.title("❤️ Assalam-o-Alaikum Baba!")
st.caption(f"📅 Aaj Ki Tareekh: {datetime.date.today().strftime('%B %d, %Y')}")
st.write("---")

# -----------------------------------------------------------------------------
# 📸 SECTION 1: 5 LOCAL PHOTOS GALLERY SLIDER
# -----------------------------------------------------------------------------
st.subheader("🖼️ Humari Pyari Yaadein (5 Special Photos)")

# 5 Photos ki List aur Unke Captions
images_data = [
    {"path": "images/pic1.jpg", "caption": "1. Aapke Saath Har Lamha Khaas Hai ❤️"},
    {"path": "images/pic2.jpg", "caption": "2. Baba — Mere Sar Ka Saaya 👑"},
    {"path": "images/pic3.jpg", "caption": "3. Aapki Smile Meri Sabse Badi Daulat 😊"},
    {"path": "images/pic4.jpg", "caption": "4. Purani Khubsurat Yaadein 📸"},
    {"path": "images/pic5.jpg", "caption": "5. Hamesha Aise Hi Muskurate Rahein! 🤲"}
]

# Slider/Selectbox to browse 5 photos
selected_idx = st.slider("Photo Badalne Ke Liye Slider Aage Karein:", 1, 5, 1) - 1

current_img = images_data[selected_idx]

# Check if image exists before rendering
if os.path.exists(current_img["path"]):
    st.image(current_img["path"], caption=current_img["caption"], use_container_width=True)
else:
    st.warning(f"⚠️ Image '{current_img['path']}' nahi mili! Barae meharbani images folder mein photo save karein.")

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
# 🤗 SECTION 3: MAGIC BUTTON
# -----------------------------------------------------------------------------
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