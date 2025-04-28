import streamlit as st
from students_data import students_data
import random

st.set_page_config(page_title="VITEX Results", page_icon="🎁", layout="centered")

# =====================
# Load ảnh hộp quà mới
# =====================
gift_images = [
    "https://cdn-icons-png.flaticon.com/512/4315/4315445.png",
    "https://cdn-icons-png.flaticon.com/512/4315/4315446.png",
    "https://cdn-icons-png.flaticon.com/512/4315/4315450.png",
    "https://cdn-icons-png.flaticon.com/512/4315/4315451.png",
    "https://cdn-icons-png.flaticon.com/512/4315/4315452.png",
]

# =====================
# Function: Hiển thị 5 hộp quà chính giữa
# =====================
def gift_box():
    st.markdown("<h2 style='text-align: center;'>🎁 Bạn đã sẵn sàng khám phá kết quả chưa?</h2>", unsafe_allow_html=True)

    # Khoảng cách trên dưới cho cân đối
    st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            st.image(gift_images[idx % len(gift_images)], width=100)
            if st.button(f"🎁 Hộp {idx+1}", key=f"gift_{idx}"):
                st.session_state["opened_gift"] = True
                st.session_state["selected_gift"] = idx

# =====================
# Function: Giao diện chọn học sinh
# =====================
def main_app():
    st.title("🎯 Kết quả học tập VITEX")

    student_name = st.selectbox("👤 Chọn tên của bạn:", list(students_data.keys()))

    if student_name:
        student = students_data[student_name]

        st.subheader(f"📝 Điểm của {student_name}")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎧 Listening", f"{student['Listening']}/10")
            st.metric("🗣️ Speaking", f"{student['Speaking']}/10")
        with col2:
            st.metric("🧠 Vocabulary", f"{student['Vocabulary']}/10")
            st.metric("🔊 Phonetics", f"{student['Phonetics']}/10")

        st.divider()

        with st.expander("💬 Nhận xét Speaking"):
            st.markdown(student['Feedback_Speaking'])

        st.divider()

        with st.expander("🌟 Nhận xét chung"):
            st.markdown(student['Feedback_Overall'])

# =====================
# MAIN APP
# =====================
if "opened_gift" not in st.session_state:
    st.session_state["opened_gift"] = False

if not st.session_state["opened_gift"]:
    gift_box()
else:
    # ===== Khi chọn xong hộp quà =====
    st.balloons()  # Hiệu ứng nổ bóng bay
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>🎉 Chúc mừng bạn đã mở được hộp quà! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

    # Thêm nút "Tiếp tục" để vào phần chính
    if st.button("🚀 Bắt đầu khám phá kết quả"):
        main_app()
