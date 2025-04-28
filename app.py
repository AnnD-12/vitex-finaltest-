import streamlit as st
from students_data import students_data

# ====================
# Font + Page setup
# ====================
st.set_page_config(page_title="VITEX Gift Game", page_icon="🎁", layout="centered")

# Inject Google Font Nunito
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Nunito', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# ====================
# Data setup
# ====================
gifts = [
    {"type": "bomb", "name": "💣 Boom"},
    {"type": "student", "name": "Anh Bách"},
    {"type": "student", "name": "Chị Huế"},
    {"type": "student", "name": "Anh Sức"},
    {"type": "student", "name": "Quỳnh"},
    {"type": "student", "name": "Tuấn"},
    {"type": "star", "name": "⭐ Star"},
]

gift_images = [
    "https://cdn-icons-png.flaticon.com/512/744/744922.png",
    "https://cdn-icons-png.flaticon.com/512/744/744932.png",
    "https://cdn-icons-png.flaticon.com/512/744/744935.png",
    "https://cdn-icons-png.flaticon.com/512/744/744934.png",
    "https://cdn-icons-png.flaticon.com/512/744/744930.png",
    "https://cdn-icons-png.flaticon.com/512/744/744926.png",
    "https://cdn-icons-png.flaticon.com/512/744/744924.png",
]

# ====================
# Session State
# ====================
if "game_state" not in st.session_state:
    st.session_state["game_state"] = "home"
if "selected_gift" not in st.session_state:
    st.session_state["selected_gift"] = None
if "opened_boxes" not in st.session_state:
    st.session_state["opened_boxes"] = []

# ====================
# Callback Functions
# ====================
def select_gift(idx):
    if idx not in st.session_state["opened_boxes"]:
        st.session_state["selected_gift"] = gifts[idx]
        st.session_state["game_state"] = "result"
        st.session_state["opened_boxes"].append(idx)

def go_home():
    st.session_state["game_state"] = "home"

# ====================
# Display Functions
# ====================
def show_home():
    st.markdown("<h2 style='text-align: center;'>🎁 Chọn một hộp quà để khám phá!</h2>", unsafe_allow_html=True)
    st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

    cols = st.columns(7)
    for idx, col in enumerate(cols):
        with col:
            st.image(gift_images[idx % len(gift_images)], width=90)
            disabled = idx in st.session_state["opened_boxes"]
            st.button(
                f"Hộp {idx+1}",
                key=f"gift_{idx}",
                on_click=select_gift,
                args=(idx,),
                disabled=disabled
            )

def show_result():
    gift = st.session_state["selected_gift"]

    if gift["type"] == "student":
        name = gift["name"]
        student = students_data[name]
        st.success(f"🎉 Bạn đã mở được hộp quà của {name}!")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎧 Listening", f"{student['Listening']}/10")
            st.metric("🧠 Vocabulary", f"{student['Vocabulary']}/10")
        with col2:
            st.metric("🔊 Phonetics", f"{student['Phonetics']}/10")
            st.metric("🗣️ Speaking", f"{student['Speaking']}/10")

        st.divider()

        with st.expander("💬 Nhận xét Speaking"):
            st.markdown(student['Feedback_Speaking'])

        st.divider()

        with st.expander("🌟 Nhận xét chung"):
            st.markdown(student['Feedback_Overall'])
        
        st.balloons()

    elif gift["type"] == "bomb":
        st.error("💣 Boom! Bạn đã chọn trúng hộp bom!")
        st.snow()

    elif gift["type"] == "star":
        st.success("⭐ Bạn thật may mắn! Nhưng đây không phải kết quả học sinh nhé!")
        st.balloons()

    st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)
    st.button("🏠 Quay về chọn hộp khác", on_click=go_home)

# ====================
# Main Control
# ====================
if st.session_state["game_state"] == "home":
    show_home()
elif st.session_state["game_state"] == "result":
    show_result()
