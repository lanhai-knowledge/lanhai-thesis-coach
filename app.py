"""嵐海知識｜論文陪跑網站｜首頁"""

from __future__ import annotations
import streamlit as st
from lib.footer import render_footer
from lib.branding import get_page_icon, render_sidebar_logo

st.set_page_config(
    page_title="嵐海知識｜論文陪跑顧問",
    page_icon=get_page_icon("🌊"),
    layout="wide",
    initial_sidebar_state="expanded",
)
render_sidebar_logo()

# === Hero ===
col_hero_text, col_hero_visual = st.columns([3, 2])

with col_hero_text:
    st.markdown(
        "<div style='color:#0062B1;font-weight:600;letter-spacing:2px;"
        "font-size:14px;margin-bottom:8px;'>嵐海知識 ・ LANHAI KNOWLEDGE</div>",
        unsafe_allow_html=True,
    )
    st.title("給卡關的你，  \n論文還是寫得出來")
    st.markdown(
        "**寫不下去？章節邏輯一直被退？口試前夜睡不著？**  \n"
        "嵐海顧問以五階段陪跑流程，"
        "協助你把論文寫到能交出去的那一刻。"
    )
    st.markdown("")
    cta_col1, cta_col2, _ = st.columns([1, 1, 2])
    with cta_col1:
        st.page_link(
            "pages/1_💼_服務方案.py", label="找到適合你的方案", icon="💼"
        )
    with cta_col2:
        st.page_link(
            "pages/3_📅_預約諮詢.py", label="預約 30 分鐘初談", icon="📅"
        )

with col_hero_visual:
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#0062B1,#3b8fd9);
                    border-radius:16px;padding:28px 32px;color:white;
                    margin-top:24px;box-shadow:0 8px 24px rgba(0,98,177,0.20);">
        <div style="opacity:0.75;font-size:13px;letter-spacing:1px;">
        數位遊牧專業顧問 ・ DIGITAL NOMAD CONSULTANT
        </div>
        <h2 style="color:white;margin:8px 0 4px 0;font-weight:600;">
        嵐嵐　Lan Lan
        </h2>
        <div style="opacity:0.75;font-size:13px;margin-bottom:18px;">
        本名：楊念慈
        </div>
        <div style="font-size:14px;line-height:1.75;opacity:0.92;
                    border-left:2px solid rgba(255,255,255,0.3);
                    padding-left:14px;font-style:italic;">
        「系統能解決的事，<br>就不該浪費你的腦力。」
        </div>
        <div style="font-size:13px;line-height:1.7;opacity:0.85;
                    margin-top:18px;">
        穿梭在不同城市的咖啡廳，<br>
        擅長把論文卡關拆解成可執行的下一步。<br>
        領航者 × 陪跑者雙重風格。
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# === 三大承諾 ===
st.markdown("## 我們的三大承諾")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### 🛡️ 不代寫")
    st.markdown(
        "嵐海顧問**不撰寫任何論文正文**。"
        "你才是作者，我們是陪跑教練——"
        "教你怎麼寫，不替你寫。"
    )
with c2:
    st.markdown("### 📋 五階段透明")
    st.markdown(
        "從**初談 → 案情分析 → 簽約 → 執行 → 結案**，"
        "每階段書面交付物明列，月度工作明細帳單可追溯。"
    )
with c3:
    st.markdown("### ⚖️ 倫理守則")
    st.markdown(
        "比照律師業專業服務模式，"
        "制定學術寫作教練倫理守則。"
        "保密義務於合約終止後 5 年仍有效。"
    )

st.markdown("---")

# === 適合對象 ===
st.markdown("## 誰適合論文陪跑")
who = st.columns(2)
with who[0]:
    st.markdown(
        "**🎯 在職進修者**  \n"
        "全職工作 + 論文兩頭燒，需要穩定節奏與外部督促。"
    )
    st.markdown(
        "**🧪 研究方法卡關者**  \n"
        "統計跑不出來、質性編碼一團亂、研究架構講不清楚。"
    )
with who[1]:
    st.markdown(
        "**✍️ 寫作節奏散掉者**  \n"
        "起頭容易、收尾困難，需要有人定期 check-in 推進度。"
    )
    st.markdown(
        "**🎤 口試前緊張者**  \n"
        "需要全真模擬、回應策略演練、PPT 診斷修訂。"
    )

st.markdown("---")

# === 五階段流程 ===
st.markdown("## 五階段標準流程")
steps = [
    ("1️⃣ 初談", "30–45 分鐘付費初談 NT$ 500（簽約後全額折抵）"),
    ("2️⃣ 案情分析", "3 日內出具需求分析書 + 方案建議書"),
    ("3️⃣ 簽約", "確認方案、簽合約與倫理守則、繳首期款"),
    ("4️⃣ 執行", "依方案進行 meeting、書面回饋、隨時諮詢"),
    ("5️⃣ 結案", "結案報告 + 學習成長摘要 + 後續建議"),
]
for label, desc in steps:
    st.markdown(f"**{label}**　{desc}")

# === 強引導 CTA ===
st.markdown("---")
st.info(
    "📅 **不確定哪個方案適合？**  \n"
    "預約 30–45 分鐘付費初談 NT$ 500（簽約後全額折抵），"
    "嵐海顧問將協助你釐清最需要的協助。"
)
cta_col1, _ = st.columns([1, 3])
with cta_col1:
    st.page_link(
        "pages/3_📅_預約諮詢.py", label="預約初談", icon="📅"
    )

render_footer()
