"""嵐海知識｜關於我們"""

from __future__ import annotations
import streamlit as st
from lib.footer import render_footer
from lib.branding import get_page_icon, render_sidebar_logo

st.set_page_config(
    page_title="關於嵐海｜嵐海知識",
    page_icon=get_page_icon("🏢"),
    layout="wide",
)
render_sidebar_logo()

st.markdown("## 🏢 關於嵐海知識")

st.markdown(
    "**嵐海知識股份有限公司**（Lanhai Knowledge Co., Ltd.）"
    "是一間專注於學術寫作教練與研究陪跑諮詢的公司。"
)

st.markdown("---")

# === 我們的定位 ===
st.markdown("### 我們的定位")
st.markdown(
    "**論文陪跑教練，不是論文代寫公司。**\n\n"
    "嵐海知識比照律師業「法律顧問」的專業服務模式，"
    "採用明確的倫理守則、標準化流程與透明收費。"
    "我們的目標是讓學員**自己寫得出來、寫得更快、寫得更好**——"
    "而不是替學員完成論文。"
)

st.markdown("")

# === 顧問 ===
st.markdown("### 顧問")

st.markdown(
    """
    <div style="background:linear-gradient(135deg,#0062B1,#3b8fd9);
                border-radius:16px;padding:32px 36px;color:white;
                box-shadow:0 8px 24px rgba(0,98,177,0.20);">
    <div style="opacity:0.75;font-size:13px;letter-spacing:1.5px;">
    數位遊牧專業顧問 ・ DIGITAL NOMAD CONSULTANT
    </div>
    <h2 style="color:white;margin:10px 0 4px 0;font-weight:600;
               font-size:32px;">
    嵐嵐　・　Lan Lan
    </h2>
    <div style="opacity:0.8;font-size:14px;margin-bottom:24px;">
    本名：楊念慈
    </div>
    <div style="font-size:15px;line-height:1.85;opacity:0.95">
    嗨，我是嵐嵐。我是念慈，也是你的數位增能夥伴。<br><br>
    我穿梭在不同城市的咖啡廳，專門解決最令人頭痛的
    系統邏輯與學術卡關。如果你正為論文煩惱，
    或是想用 Claude Code 打造更流暢的開發環境，
    甚至想優化公司的整體架構，我都在這。<br><br>
    我的目標很簡單：<br>
    <strong style="font-size:17px;">用最強的 AI 技術，
    還你最自由的生活。</strong>
    </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown("")

# === 核心使命 ===
st.markdown("#### 🎯 核心使命")
st.markdown(
    "透過**技術自動化**與**系統整合**，釋放人們的創造力——"
    "讓專業人士能在世界任何角落高效產出。"
)

st.markdown("")

# === 雙重風格 ===
st.markdown("#### 🧭 領航者 × 陪跑者　雙重風格")
c1, c2 = st.columns(2)
with c1:
    st.markdown(
        "**🛟 領航者 (Pilot)**  \n"
        "面對複雜的系統問題時，沉穩且充滿邏輯。"
        "把混亂的研究架構、跑不通的分析流程、"
        "卡關的程式邏輯，一層一層拆給你看。"
    )
with c2:
    st.markdown(
        "**🤝 陪跑者 (Supporter)**  \n"
        "面對寫論文的焦慮者，溫柔、耐心，且具備同理心。"
        "知道在職進修者多累，所以節奏由你決定，"
        "嵐嵐只是穩穩走在旁邊。"
    )

st.markdown("")

# === 四大專業 ===
st.markdown("#### 🛠️ 四大專業領域")
e1, e2 = st.columns(2)
with e1:
    st.markdown(
        "**📚 學術論文陪跑**  \n"
        "針對研究生與研究人員，提供從構論、文獻整理"
        "到寫作邏輯的 AI 協作引導。"
    )
    st.markdown(
        "**⚡ Claude Code 實戰**  \n"
        "擅長運用 AI 開發者工具進行高效率的"
        "程式碼開發與問題診斷。"
    )
with e2:
    st.markdown(
        "**🔗 系統架構整合**  \n"
        "串接不同數位工具（CRM、自動化工作流），"
        "優化企業營運效率。"
    )
    st.markdown(
        "**🏢 企業戰略諮詢**  \n"
        "協助公司進行數位轉型，"
        "解決技術落差與流程瓶頸。"
    )

st.caption("📌 本網站聚焦於「學術論文陪跑」服務；其他三項領域請來信洽詢。")

st.markdown("")

# === 口頭禪 ===
st.markdown("#### 💬 嵐嵐的三句話")
st.markdown(
    """
    > 「系統能解決的事，就不該浪費你的腦力。」

    > 「讓我們把這段邏輯拆解一下，其實沒那麼難。」

    > 「今天你在哪裡工作？我們開始吧！」
    """
)

st.markdown("")

# === 我們的承諾 ===
st.markdown("### 我們的承諾")
c1, c2 = st.columns(2)
with c1:
    st.markdown(
        "**可以做的事 ✅**\n"
        "- 題目聚焦與研究問題診斷\n"
        "- 文獻檢索策略、資料庫操作教學\n"
        "- 研究架構與章節邏輯診斷\n"
        "- 量化／質性資料分析協助（SPSS、R）\n"
        "- 統計表格、圖表產製指導\n"
        "- APA 格式、引用管理工具教學\n"
        "- 逐章編修與潤稿（你先寫，我們幫你改）\n"
        "- 口試前模擬與回應策略"
    )
with c2:
    st.markdown(
        "**不做的事 ❌**\n"
        "- 代寫任何一段論文正文\n"
        "- 代為回應口委意見（可討論方向，但筆要你自己動）\n"
        "- 偽造或美化數據\n"
        "- 「口試通過才付款」式後酬\n"
        "- 保證口試通過、學位授予或期刊接受\n"
        "- 未經學員同意公開個人資訊或論文內容"
    )

st.markdown("")

# === 服務理念 ===
st.markdown("### 服務理念")
st.markdown(
    "> 市場上論文指導服務普遍在 NT$ 7.5 萬～10 萬以上，"
    "嵐海知識選擇用半價提供相同品質的服務，"
    "是因為我們相信：\n>\n"
    "> **論文寫作的陪跑，本該是一種教育，"
    "而不只是一種商品。**\n>\n"
    "> 學員帶走的不只是一本論文，"
    "還有日後自己也能完成研究的能力。"
)

st.markdown("---")

# === 聯絡方式 ===
st.markdown("### 聯絡方式")
st.markdown(
    "**嵐海知識股份有限公司**  \n"
    "Lanhai Knowledge Co., Ltd.  \n\n"
    "📧 Email：lanlanio1103@gmail.com  \n"
    "💬 LINE：`pulovemo`（加好友請註明來自嵐海知識網站）"
)

render_footer()
