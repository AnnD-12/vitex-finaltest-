import streamlit as st
from students_data import students_data

st.set_page_config(page_title="VITEX Results", page_icon="🎁", layout="centered")

# =====================
# Function: Hiển thị màn mở hộp quà
# =====================
def gift_box():
    st.image("https://i.imgur.com/C3p8ZnG.png", width=300)  # Hình hộp quà
    st.markdown("<h3 style='text-align: center;'>🎁 Bạn đã sẵn sàng khám phá chưa?</h3>", unsafe_allow_html=True)
    if st.button("🚀 Mở Hộp Quà"):
        st.session_state["opened_gift"] = True

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
    main_app()
