"""嵐海知識｜全站法律免責 footer"""

from __future__ import annotations
import streamlit as st


DISCLAIMER_TEXT = """
本網站由 **嵐海知識股份有限公司** 營運，提供論文寫作教練與學術陪跑諮詢服務。

**服務承諾與紅線**
- 我們協助學員自己完成論文，**不代寫**任何論文正文段落
- 顧問**不掛名**為共同作者，所有學術產出歸學員本人
- 我們**不保證**口試通過、學位授予或期刊接受
- 顧問服務遵守學術倫理規範；學員上傳之資料僅用於諮詢分析，不另作他用

**收費與合約**
所有正式服務均以書面合約為準，付款後開立收據或發票。

**公開資訊**
完整版的「研究教練倫理守則 v1.0」與「服務合約範本」，
將於初談後 3 日內隨「需求分析書 + 方案建議書」一併提供。
本網站採用無障礙設計準則，文字與背景對比度符合 WCAG 2.2 AA 規範。
"""


def render_footer() -> None:
    st.markdown("---")
    with st.expander("⚖️ 服務條款 ・ 學術倫理 ・ 無障礙聲明", expanded=False):
        st.markdown(DISCLAIMER_TEXT)
    st.caption(
        "© 嵐海知識股份有限公司 ・ Lanhai Knowledge Co., Ltd. ・ "
        "聯絡 email：lanlanio1103@gmail.com ・ LINE：pulovemo"
    )
