"""嵐海知識｜預約諮詢"""

from __future__ import annotations
import streamlit as st
from lib.footer import render_footer
from lib.branding import get_page_icon, render_sidebar_logo
from lib.mailer import (
    MailerConfigError,
    format_booking_body,
    send_booking_email,
)

st.set_page_config(
    page_title="預約諮詢｜嵐海知識",
    page_icon=get_page_icon("📅"),
    layout="wide",
)
render_sidebar_logo()

st.markdown("## 📅 預約諮詢")
st.markdown(
    "**初談 30–45 分鐘 ・ NT$ 500 ・ 簽約後全額折抵**"
)

st.markdown(
    """
    > 「**讓我們把這段邏輯拆解一下，其實沒那麼難。**」
    >
    > —— 嵐嵐 ・ 數位遊牧專業顧問
    """
)

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 為什麼採付費初談？")
    st.markdown(
        "比照律師業做法，付費初談有三個目的：\n\n"
        "1. **提升雙方嚴肅度**——願意付 500 元的人，"
        "通常也願意認真考慮後續合作\n"
        "2. **過濾不匹配客戶**——省下雙方時間\n"
        "3. **簽約後全額折抵**——不影響真正有意願的學員\n\n"
        "500 元門檻極低，不會造成實質負擔，"
        "但能讓我們在 30–45 分鐘內聚焦在你**真正的問題**上。"
    )

with c2:
    st.markdown("### 初談會聊什麼？")
    timeline = [
        ("0–5 min", "嵐嵐自我介紹 + 倫理守則重點宣讀"),
        ("5–20 min", "「先讓我聽你說，論文現在卡在哪？」"),
        ("20–35 min", "初步診斷 + 邏輯拆解，「其實沒那麼難」"),
        ("35–45 min", "建議可能合作模式 + 說明下一步"),
    ]
    for t, desc in timeline:
        st.markdown(f"**{t}**　{desc}")
    st.caption("初談結束後 3 日內，將寄送「需求分析書 + 方案建議書」PDF。")

st.markdown("---")

# === 預約表單 ===
st.markdown("### 線上預約")
st.caption(
    "填寫以下資訊後，嵐海顧問將於 1–2 個工作天內以 email 回覆確認。"
    "（必填欄位以 * 標示）"
)

with st.form("booking_form"):
    name = st.text_input("您的稱呼 *")
    email = st.text_input("Email *")
    line_id = st.text_input("LINE ID（選填）")

    school_program = st.text_input(
        "目前就讀階段（選填）",
        placeholder="例：碩士生在職專班 / 博士生 / 已申請學校尚未入學",
    )

    topic = st.text_area(
        "論文主題或領域 *（一句話即可）",
        placeholder="例：探討 AI 工具對中小學教師備課歷程的影響",
        height=80,
    )

    pain_point = st.text_area(
        "目前最想解決的問題 *",
        placeholder=(
            "例：題目方向不確定／統計方法不會選／"
            "文獻探討一直被退／口試前焦慮..."
        ),
        height=120,
    )

    preferred_time = st.multiselect(
        "偏好初談時段（可複選）",
        [
            "平日晚上（19:00–22:00）",
            "週六上午",
            "週六下午",
            "週日上午",
            "週日下午",
        ],
    )

    interested_plan = st.selectbox(
        "目前較有興趣的方案（可後續調整）",
        [
            "尚未決定，希望初談後再評估",
            "L1 鐘點諮詢（NT$ 1,500 / 60 min）",
            "L2 論件計酬（NT$ 1,500–3,000 / 件）",
            "L3 階段陪跑（NT$ 10,000–28,000）",
            "L4 全程教練（NT$ 50,000）",
            "L5 月費顧問（NT$ 5,000–8,000 / 月）",
        ],
    )

    consent = st.checkbox(
        "我已閱讀並同意嵐海知識的服務條款與學術倫理聲明 *",
    )

    submitted = st.form_submit_button("送出預約", type="primary")

    if submitted:
        if not (name and email and topic and pain_point and consent):
            st.error("請填寫必填欄位（標 * 者）並勾選同意條款。")
        else:
            body = format_booking_body(
                {
                    "稱呼": name,
                    "Email": email,
                    "LINE ID": line_id,
                    "就讀階段": school_program,
                    "論文主題": topic,
                    "目前最想解決的問題": pain_point,
                    "偏好初談時段": preferred_time,
                    "有興趣的方案": interested_plan,
                }
            )
            try:
                send_booking_email(
                    subject=f"【嵐海預約】{name}｜{interested_plan}",
                    body=body,
                    reply_to=email,
                )
            except MailerConfigError as exc:
                st.error(
                    "❌ 預約寄送失敗（系統設定不完整）。"
                    "請改以信件聯絡 b0915905438@gmail.com，"
                    "並截圖以下訊息給站務："
                )
                st.code(str(exc))
            except Exception as exc:  # noqa: BLE001
                st.error(
                    "❌ 預約寄送失敗。請改以信件聯絡 "
                    "b0915905438@gmail.com，並附上下列錯誤訊息："
                )
                st.code(f"{type(exc).__name__}: {exc}")
            else:
                st.success(
                    "✅ 預約資訊已寄出。"
                    "嵐海顧問將於 1–2 個工作天內以 email 回覆確認。"
                )

st.markdown("---")
st.markdown("### 其他聯絡方式")
st.markdown(
    "- **Email**：b0915905438@gmail.com\n"
    "- **LINE**：`pulovemo`（加好友請註明來自嵐海知識網站）\n"
    "- **Email 主旨**：請註明「論文陪跑諮詢」+ 您的稱呼"
)

render_footer()
