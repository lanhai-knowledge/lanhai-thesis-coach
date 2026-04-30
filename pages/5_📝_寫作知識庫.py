"""嵐海知識｜寫作知識庫（blog 形式 + 分類）"""

from __future__ import annotations
import streamlit as st
from lib.footer import render_footer
from lib.articles import list_articles, get_article, list_categories

st.set_page_config(
    page_title="寫作知識庫｜嵐海知識",
    page_icon="📝",
    layout="wide",
)

# ---- 路由：?article=<slug> 進入單篇；無 query 顯示列表 ----
slug = st.query_params.get("article", None)

if slug:
    article = get_article(slug)
    if not article:
        st.error("找不到這篇文章。")
        st.page_link("pages/5_📝_寫作知識庫.py", label="← 回到知識庫")
        render_footer()
        st.stop()

    # === 單篇文章視圖 ===
    st.markdown(
        f"<a href='?' style='color:#0062B1;text-decoration:none;'>"
        f"← 回到知識庫列表</a>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='color:#0062B1;font-weight:600;letter-spacing:1.5px;"
        f"font-size:13px;margin:20px 0 8px 0;'>"
        f"{article.category.upper()}</div>",
        unsafe_allow_html=True,
    )
    st.title(article.title)
    st.caption(
        f"📅 {article.date_label}　・　"
        f"✍️ {article.author}　・　"
        f"⏱ 閱讀時間約 {article.read_time} 分鐘"
    )
    if article.tags:
        tag_html = " ".join(
            f"<span style='background:#eef3f7;color:#1f2937;"
            f"padding:3px 10px;border-radius:12px;"
            f"font-size:12px;margin-right:6px;'>#{t}</span>"
            for t in article.tags
        )
        st.markdown(tag_html, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(article.body)

    st.markdown("---")
    st.info(
        "💡 **這篇對你有幫助嗎？**  \n"
        "嵐海顧問提供完整的論文陪跑服務——從文獻檢索、APA 格式、"
        "到口試衝刺，五階段陪你走完。"
    )
    c1, _ = st.columns([1, 3])
    with c1:
        st.page_link(
            "pages/3_📅_預約諮詢.py", label="預約初談", icon="📅"
        )

    render_footer()
    st.stop()

# === 列表視圖 ===
st.markdown("## 📝 寫作知識庫")
st.markdown(
    "嵐嵐整理的論文寫作實戰心法，"
    "涵蓋文獻檢索、研究方法、APA 格式、AI 工具運用、"
    "口試衝刺等主題——**完全免費，希望你寫得順一點**。"
)

articles = list_articles()
categories = list_categories(articles)

if not articles:
    st.info("尚未發布文章，敬請期待。")
    render_footer()
    st.stop()

# === 分類 filter ===
st.markdown("---")

filter_col, count_col = st.columns([3, 1])
with filter_col:
    selected_cat = st.radio(
        "依分類篩選",
        ["全部"] + categories,
        horizontal=True,
        label_visibility="collapsed",
    )
with count_col:
    if selected_cat == "全部":
        st.caption(f"共 {len(articles)} 篇")
    else:
        n = sum(1 for a in articles if a.category == selected_cat)
        st.caption(f"{selected_cat}：{n} 篇")

st.markdown("")

# === 文章卡片 grid ===
filtered = [
    a for a in articles
    if selected_cat == "全部" or a.category == selected_cat
]

# 一行 2 卡
for i in range(0, len(filtered), 2):
    cols = st.columns(2)
    for j, art in enumerate(filtered[i : i + 2]):
        with cols[j]:
            st.markdown(
                f"""
                <div style='border:1px solid #d6dde4;border-radius:12px;
                            padding:24px;background:white;
                            margin-bottom:12px;height:240px;
                            display:flex;flex-direction:column;
                            justify-content:space-between;'>
                <div>
                <div style='color:#0062B1;font-weight:600;
                            letter-spacing:1.5px;font-size:12px;
                            margin-bottom:8px;'>
                {art.category.upper()}
                </div>
                <h4 style='margin:0 0 12px 0;color:#1f2937;
                           font-size:18px;line-height:1.4;'>
                {art.title}
                </h4>
                <p style='color:#475569;font-size:14px;line-height:1.6;
                          margin:0 0 12px 0;'>
                {art.summary}
                </p>
                </div>
                <div style='color:#94a3b8;font-size:12px;'>
                📅 {art.date_label}　・　⏱ {art.read_time} min
                </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # st.page_link 不支援 query param，改用 anchor 帶 ?article=<slug>
            st.markdown(
                f"<a href='?article={art.slug}' "
                f"style='display:inline-block;color:#0062B1;"
                f"font-weight:600;text-decoration:none;"
                f"margin-bottom:24px;'>"
                f"閱讀全文 →</a>",
                unsafe_allow_html=True,
            )

if not filtered:
    st.info(f"分類「{selected_cat}」目前還沒有文章。")

render_footer()
