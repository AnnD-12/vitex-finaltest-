import streamlit as st
from students_data import students_data

st.set_page_config(page_title="VITEX Results", page_icon="📚")

st.title("🎯 Kết quả học tập VITEX")

# ==== Chọn học sinh ====
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
        st.write(student['Feedback_Speaking'])

    with st.expander("🌟 Nhận xét chung"):
        st.write(student['Feedback_Overall'])
