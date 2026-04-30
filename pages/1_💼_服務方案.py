"""嵐海知識｜服務方案"""

from __future__ import annotations
import streamlit as st
from lib.footer import render_footer

st.set_page_config(
    page_title="服務方案｜嵐海知識",
    page_icon="💼",
    layout="wide",
)

st.markdown("## 💼 服務方案")
st.markdown(
    "嵐海知識提供五種計費模式，"
    "從單次鐘點諮詢到全程教練，"
    "對應在職進修者不同階段的需求。"
)
st.caption("⏰ 推廣期價格為市場中位數的 1/2，名額有限。")

st.markdown("---")

# === L1 ===
st.markdown("### 🔵 L1 ｜ 鐘點諮詢")
c = st.columns([1, 2])
with c[0]:
    st.metric("60 分鐘", "NT$ 1,500")
    st.caption("市場中位數約 3,000–5,000")
with c[1]:
    st.markdown(
        "**適合**：單點問題、想試水溫、不願承諾長期合作  \n"
        "**形式**：線上 Google Meet 為主，實體需另議  \n"
        "**交付**：會議紀錄 + 口頭建議  \n"
        "**加購**：90 分鐘版 NT$ 2,000、會後書面摘要 +NT$ 500（1 頁）"
    )

st.markdown("")

# === L2 ===
st.markdown("### 🟣 L2 ｜ 論件計酬")
c = st.columns([1, 2])
with c[0]:
    st.metric("單件", "NT$ 1,500–3,000")
    st.caption("適合明確具體任務")
with c[1]:
    items = [
        ("📚 文獻檢索包", "NT$ 2,000", "20 篇文獻 + 分級清單（⭐⭐⭐/⭐⭐/⭐）+ 來源連結"),
        ("📝 單章 APA 格式校對", "NT$ 1,500", "格式修正 + 引用檢查 + 參考文獻排版"),
        ("📊 SPSS/R 統計單案", "NT$ 3,000", "跑分析 + 解讀報告（含圖表）"),
        ("🎤 口試 PPT 診斷", "NT$ 2,500", "書面回饋 + 修改建議（5–8 頁）"),
        ("✏️ 單章潤稿（5,000 字內）", "NT$ 2,000", "結構建議 + 語句優化（不代寫）"),
    ]
    for name, price, desc in items:
        st.markdown(f"- **{name}**　{price}　— {desc}")
    st.caption("📦 包套優惠：任選 3 項 85 折、5 項 75 折")

st.markdown("")

# === L3 ===
st.markdown("### 🟡 L3 ｜ 階段陪跑")
c = st.columns([1, 2])
with c[0]:
    st.metric("整段陪跑", "NT$ 10,000–28,000")
    st.caption("每階段 4–8 週")
with c[1]:
    stages = [
        ("A. 計畫書衝刺", "NT$ 15,000", "題目→文獻→研究方法定稿，2 次 meeting + 1 次書面回饋"),
        ("B. 資料蒐集與分析", "NT$ 18,000", "工具設計、訪談大綱、量化／質性分析協助"),
        ("C. 論文撰寫陪跑", "NT$ 28,000", "四~五章逐章診斷 + 潤稿，3 次 meeting"),
        ("D. 口試前衝刺", "NT$ 10,000", "PPT 診斷、模擬口試、回應策略、論文修訂"),
    ]
    for name, price, desc in stages:
        st.markdown(f"- **{name}**　{price}　— {desc}")
    st.caption("付款：簽約 50% / 階段完成 50%")

st.markdown("")

# === L4 ===
st.markdown("### 🟢 L4 ｜ 全程教練")
c = st.columns([1, 2])
with c[0]:
    st.metric("從開題到口試", "NT$ 50,000")
    st.caption("市場中位數約 100,000")
with c[1]:
    st.markdown(
        "**期程**：6–12 個月  \n"
        "**頻率**：每兩週一次定期 meeting（60–90 分鐘）  \n"
        "**諮詢**：全程 LINE/Email 諮詢（48 小時內回覆）  \n"
        "**交付**：四階段書面診斷報告 + 口試前全真模擬一次  \n"
        "**保障**：若未能在期程內順利口試，可延長 3 個月不加價  \n"
        "**分期**：簽約 30% / 計畫書通過 30% / 口試通過 40%"
    )

st.markdown("")

# === L5 ===
st.markdown("### 🔴 L5 ｜ 月費顧問")
c = st.columns([1, 2])
with c[0]:
    st.metric("基本版", "NT$ 5,000 / 月")
    st.metric("進階版", "NT$ 8,000 / 月")
    st.caption("彈性升降級")
with c[1]:
    st.markdown(
        "**基本版（NT$ 5,000）**：每月 4 小時服務額度（meeting/書面/諮詢可混用）"
        "+ LINE/Email 無限諮詢（48 hr 回覆）+ 月度工作明細帳單  \n\n"
        "**進階版（NT$ 8,000）**：每月 8 小時 + 優先預約權 + 月度進度報告  \n\n"
        "**特色**：未用時數可結轉至下月（不超過 2 個月）、隨時升降級、"
        "隨時停止（提前 14 天通知）、**前 3 個月不漲價保證**"
    )
    st.caption("適合不趕時程、想穩定陪跑、按月彈性付款的學員")

st.markdown("---")

# === 收費透明度 ===
st.markdown("### 📄 月度工作明細帳單（L4、L5 適用）")
st.markdown(
    "嵐海知識比照律師業做法，每月月底寄送工作明細，"
    "讓學員清楚知道顧問的每一分投入：\n\n"
    "- 每次 meeting 的時長與主題\n"
    "- 書面回饋的篇幅與重點\n"
    "- LINE 諮詢的次數與時數累計\n"
    "- 本月剩餘額度（可結轉）\n"
    "- 本月亮點 + 下月重點"
)

st.markdown("---")

# === CTA ===
st.info(
    "💡 **不確定哪個方案適合你？**  \n"
    "預約 30–45 分鐘付費初談 NT$ 500（簽約後全額折抵），"
    "嵐海顧問將根據你的論文現況推薦最適合的服務組合。"
)
c1, _ = st.columns([1, 3])
with c1:
    st.page_link(
        "pages/3_📅_預約諮詢.py", label="預約初談", icon="📅"
    )

render_footer()
