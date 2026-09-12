import time
import streamlit as st

st.title("เกมทดสอบความรู้เรื่องสี 🌈🎨🖌️")

# 1. Initialize session_state defaults
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""


# Function to reset game state
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# Result Dialog
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    # Question 1
    if u_ans1 in ["7 สี", "7", "7สี"]:
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # Question 2
    if u_ans2 in ["3 สี", "3", "3สี"]:
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # Question 3
    if u_ans3 in ["สีบานเย็น", "บานเย็น", "สี บานเย็น"]:
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # Question 4
    if u_ans4 in [
        "สีม่วง สีเหลือง",
        "สีม่วงสีเหลือง",
        "ม่วง เหลือง",
        "ม่วงเหลือง",
        "สีเหลือง สีม่วง",
        "สีเหลืองสีม่วง",
        "เหลือง ม่วง",
        "เหลืองม่วง",
    ]:
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # Question 5
    if u_ans5 in [
        "80% ต่อ 20%",
        "80 ต่อ 20",
        "80 / 20",
        "80/20",
        "80:20",
    ]:
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("🎉 ชนะ!")
    elif score in [3, 4]:
        st.info("👌 พยายามอีกนิด!")
    else:
        st.error("💀 แพ้")


# ----------------------------------------------------
# Game Interface
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# Countdown timer logic
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# Inputs
ans1 = st.text_input("ข้อ 1: สายรุ้งมีกี่สี ❓", value=st.session_state.ans1_val)
ans2 = st.text_input("ข้อ 2: ธงชาติไทยมีกี่สี ❓", value=st.session_state.ans2_val)
ans3 = st.text_input(
    "ข้อ 3: สีประจำโรงเรียนยุพราชคือสีอะไร ❓",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: สีคู่ตรงข้ามที่อยู่ได้สองวรรณะคือสีอะไรบ้าง ❓",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: สีคู่ตรงข้าม ควรใช้ยังไง ❓ (ตอบเป็นอัตราส่วน)",
    value=st.session_state.ans5_val,
)

# Store responses
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

# Submit Button
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

# Display Result Dialog
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)

st.divider()
st.write("""
นางสาว อริสรา ธัชช์ชยกุล เลขที่ 4 ม.4/3,
นางสาว สาริสา ขันธนา เลขที่ 5 ม.4/3,
นางสาว ฉัตรดรุณี ธนะปัญโญ เลขที่ 17 ม.4/3,
นางสาว เฌอเอม เหล่าเขตรกิจ เลขที่ 39 ม.4/3
""")
