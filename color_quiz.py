import time
import streamlit as st

st.title("เกมทดสอบความรู้เรื่องสี 🌈🎨🖌️")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "7 สี":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    or u_ans1 == "7":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    or u_ans1 == "7สี":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "3 สี":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    or u_ans2 == "3":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    or u_ans2 == "3สี":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ตรวจข้อ 3
    if u_ans3 == "สีบานเย็น":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    or u_ans3 == "บานเย็น":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    or u_ans3 == "สี บานเย็น":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "สีม่วง สีเหลือง":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    or u_ans4 == "สีม่วงสีเหลือง":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    or u_ans4 == "ม่วง เหลือง":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    or u_ans4 == "ม่วงเหลือง":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
      
    # ตรวจข้อ 5
    if u_ans5 == "80% ต่อ 20%":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    if u_ans5 == "80 ต่อ 20":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    if u_ans5 == "80 / 20":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    if u_ans5 == "80/20":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    if u_ans5 == "80:20":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    
st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("🎉 ชนะ!")
    or score == 3 or 4:
        st.success("👌 พยายามอีกนิด!")
    else:
      if score == 0 or 1 or 2:
        st.error("💀 แพ้")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: สายรุ้งมีกี่สี ❓",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: ธงชาติไทยมีกี่สี ❓",
    value=st.session_state.ans2_val,
)
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
# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)

st.divider()
st.write(
"นางสาว อริสรา ธัชช์ชยกุล เลขที่ 4 ม.4/3
นางสาว สาริสา ขันธนา เลขที่ 5 ม.4/3
นางสาว ฉัตรดรุณี ธนะปัญโญ เลขที่ 17 ม.4/3
นางสาว เฌอเอม เหล่าเขตรกิจ เลขที่ 39 ม.4/3"
)
