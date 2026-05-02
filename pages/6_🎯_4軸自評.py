"""嵐海知識｜一人化公司 4 軸自評（lead magnet）"""

from __future__ import annotations
import streamlit as st
import plotly.graph_objects as go
from lib.footer import render_footer
from lib.branding import get_page_icon, render_sidebar_logo

st.set_page_config(
    page_title="4 軸自評｜嵐海知識",
    page_icon=get_page_icon("🎯"),
    layout="wide",
)
render_sidebar_logo()

# ============= 題目資料 =============
AXES = [
    {
        "key": "writing",
        "emoji": "✍️",
        "name": "寫作軸",
        "en": "Writing",
        "tagline": "知識生產",
        "question": "你能不能持續產出有結構的文字內容？",
        "items": [
            "我每週至少寫一次超過 1000 字的內容",
            "我有自己的寫作系統（地點 / 工具 / 節奏）",
            "我有寫成的東西被別人付費 / 引用 / 採用",
            "我能在 1 小時內寫出 800 字結構合理的初稿",
            "我用 AI 工具輔助寫作（不是代寫）",
            "我有自己的發佈平台（部落格 / 電子報 / 社群）",
        ],
        "service": "論文 / 書稿陪跑、AI 輔助寫作",
        "trial": "L1 鐘點諮詢 NT$ 1,500 / L5 月費 NT$ 5,000",
    },
    {
        "key": "building",
        "emoji": "🛠️",
        "name": "開發軸",
        "en": "Building",
        "tagline": "產品化",
        "question": "你能不能把想法變成可運行的產品？",
        "items": [
            "我自己做的數位產品 / 工具目前還在運行",
            "我會改 / 修 / 部署簡單的網站或程式",
            "我能用 no-code 工具（Notion / Airtable / Zapier）做出工作流",
            "我能用 AI Coding 工具（Claude Code / Cursor / v0）產出原型",
            "我有自架的網站或工具（不只是用平台託管）",
            "我做的東西有人付費使用",
        ],
        "service": "軟體開發顧問、SaaS 原型陪跑",
        "trial": "論件計酬 / 月費（依案件複雜度）",
    },
    {
        "key": "digitalization",
        "emoji": "🌐",
        "name": "數位化軸",
        "en": "Digitalization",
        "tagline": "服務商業化",
        "question": "你的服務能不能不見面就完成？",
        "items": [
            "我的服務 80% 以上可以遠距完成",
            "我有線上預約系統（Calendly / Cal.com / 其他）",
            "我有電子合約 + 線上付款流程",
            "我有完整的客戶 SOP（從詢問到結案）",
            "我能離開家鄉超過 1 個月仍正常服務客戶",
            "我的服務有現成的說明 / 報價單 / brochure",
        ],
        "service": "數位化諮詢、線上交付流程設計",
        "trial": "階段陪跑（B 資料 / SOP 建置）",
    },
    {
        "key": "ops",
        "emoji": "⚙️",
        "name": "工作流軸",
        "en": "Ops / AI",
        "tagline": "系統自動化",
        "question": "你的「重複勞動」有沒有用 AI 減負？",
        "items": [
            "我每天用 AI 工具（Claude / GPT / Gemini）超過 30 分鐘",
            "我有自己的「第二大腦」系統（Obsidian / Notion / Logseq 等）",
            "我有自動化的 email / 行事曆 / 文件管理流程",
            "我能用 prompt 或 agent 處理重複任務",
            "我每週花在「行政雜事」少於 5 小時",
            "我有版本控制 / 自動備份習慣",
        ],
        "service": "AI 工具導入、自動化 pipeline",
        "trial": "鐘點諮詢 / 工作坊試水",
    },
]

OPTIONS = {0: "0 完全沒有", 1: "1 部分到位", 2: "2 完全做到"}

# ============= Header =============
st.markdown("## 🎯 一人化公司 4 軸自評")
st.markdown(
    "**給數位遊牧者 / Solopreneur / 一人化知識工作者**　\n"
    "30 秒看出你最該補哪根技術骨架。"
)
st.caption("⏱️ 24 題自評，提交後立即看到 4 軸雷達圖 + 個人化建議")

with st.expander("為什麼是 4 軸？"):
    st.markdown(
        "數位遊牧者多半是「一人化公司」── 一個人扛起整個事業。"
        "但事業要活下來，需要 4 根技術骨架同時撐住：\n\n"
        "1. **寫作軸 ✍️** ─ 知識生產（論文 / 書 / 報告 / 長文）\n"
        "2. **開發軸 🛠️** ─ 產品化（產品 / 工具 / SaaS）\n"
        "3. **數位化軸 🌐** ─ 服務商業化（遠距 / 線上 / SOP）\n"
        "4. **工作流軸 ⚙️** ─ 系統自動化（AI / 第二大腦 / pipeline）\n\n"
        "多數 solopreneur 的卡點：2-3 軸還行，1-2 軸是空的或瘸的。"
        "**這份量表的用途**：30 秒看出你哪根骨架最該補。"
    )

st.markdown("---")

# ============= Form =============
with st.form("axis_form"):
    scores: dict[str, list[int]] = {}
    for axis in AXES:
        st.markdown(f"### {axis['emoji']} {axis['name']}　_{axis['en']} ─ {axis['tagline']}_")
        st.markdown(f"**{axis['question']}**")
        scores[axis["key"]] = []
        for i, item in enumerate(axis["items"]):
            choice = st.radio(
                f"{i+1}. {item}",
                options=list(OPTIONS.keys()),
                format_func=lambda x: OPTIONS[x],
                horizontal=True,
                key=f"{axis['key']}_{i}",
            )
            scores[axis["key"]].append(choice)
        st.markdown("")

    submitted = st.form_submit_button(
        "📊 查看我的雷達圖", use_container_width=True, type="primary"
    )

# ============= Result =============
if submitted:
    st.markdown("---")
    st.markdown("# 📊 你的 4 軸結果")

    totals = {axis["key"]: sum(scores[axis["key"]]) for axis in AXES}
    grand_total = sum(totals.values())
    weakest_key = min(totals, key=totals.get)
    weakest_axis = next(a for a in AXES if a["key"] == weakest_key)

    # 階段判定
    if grand_total <= 15:
        phase, phase_emoji, phase_advice = (
            "初出茅廬",
            "🌱",
            "建議系統性陪跑（全程教練 NT$ 50,000 / 6-12 個月）",
        )
    elif grand_total <= 30:
        phase, phase_emoji, phase_advice = (
            "典型 solopreneur 困境",
            "🧗",
            "月費顧問（NT$ 5,000-8,000）長期撐 + 階段陪跑補單軸",
        )
    elif grand_total <= 40:
        phase, phase_emoji, phase_advice = (
            "已成型一人公司",
            "🚀",
            "點對點諮詢 + 工作流優化",
        )
    else:
        phase, phase_emoji, phase_advice = (
            "Solopreneur Pro",
            "💎",
            "嵐海可作為「特定問題」的諮詢顧問，或互為合作對象",
        )

    # 雷達圖 + 數據面板
    axis_labels = [f"{a['emoji']} {a['name']}" for a in AXES]
    r_values = [totals[a["key"]] for a in AXES]
    axis_labels.append(axis_labels[0])
    r_values.append(r_values[0])

    fig = go.Figure(
        data=go.Scatterpolar(
            r=r_values,
            theta=axis_labels,
            fill="toself",
            line=dict(color="#0062B1", width=3),
            fillcolor="rgba(0, 98, 177, 0.25)",
            name="你的 4 軸",
        )
    )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 12],
                tickmode="linear",
                tick0=0,
                dtick=3,
                gridcolor="#DDD",
            ),
            angularaxis=dict(tickfont=dict(size=14)),
            bgcolor="#FAFAFA",
        ),
        showlegend=False,
        height=500,
        margin=dict(l=80, r=80, t=40, b=40),
    )

    c1, c2 = st.columns([3, 2])
    with c1:
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        st.metric("總分", f"{grand_total} / 48")
        st.markdown(f"### {phase_emoji} **{phase}**")
        st.caption(phase_advice)
        st.markdown("**各軸得分**：")
        for axis in AXES:
            score = totals[axis["key"]]
            if score <= 4:
                color = "🔴"
            elif score <= 8:
                color = "🟡"
            else:
                color = "🟢"
            st.markdown(f"- {color} {axis['emoji']} {axis['name']}：**{score}** / 12")

    st.markdown("---")

    # 緊急瓶頸
    st.markdown(
        f"### 🎯 你的緊急瓶頸：{weakest_axis['emoji']} {weakest_axis['name']}"
    )

    weakest_score = totals[weakest_key]
    if weakest_score <= 3:
        urgency, urgency_advice = (
            "🔴 紅燈（緊急）",
            "這軸完全空，建議從單軸鐘點諮詢試水",
        )
    elif weakest_score <= 6:
        urgency, urgency_advice = (
            "🟡 黃燈（部分到位）",
            "部分到位但常卡關，月費基本版可長期撐住",
        )
    elif weakest_score <= 9:
        urgency, urgency_advice = (
            "🟢 綠燈（大致 OK）",
            "大致 OK，論件計酬處理單點問題即可",
        )
    else:
        urgency, urgency_advice = (
            "⭐ 強項（不需介入）",
            "這軸是你的優勢，可考慮把這軸服務化變產品",
        )

    st.info(f"**得分：{weakest_score} / 12 ─ {urgency}**\n\n{urgency_advice}")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**嵐海對應服務**：{weakest_axis['service']}")
    with c2:
        st.markdown(f"**推薦試水方案**：{weakest_axis['trial']}")

    st.markdown("---")

    # CTA
    st.markdown("### 📞 下一步")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.page_link("pages/1_💼_服務方案.py", label="看完整服務方案", icon="💼")
    with c2:
        st.page_link("pages/3_📅_預約諮詢.py", label="預約付費初談", icon="📅")
    with c3:
        st.page_link("pages/4_🏢_關於嵐海.py", label="認識嵐海", icon="🏢")

    st.caption("💡 30 分鐘付費初談 NT$ 500，簽約後全額折抵")

render_footer()
