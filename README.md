# 嵐海知識｜論文陪跑網站（lanhai-thesis-coach）

嵐海知識股份有限公司對外網站，提供論文寫作教練與學術陪跑諮詢服務。

## Stack

- Streamlit + Anthropic API
- Python 3.11
- 部署：Streamlit Cloud

## 結構

```
lanhai-thesis-coach/
├── app.py                       # 首頁
├── pages/
│   ├── 1_💼_服務方案.py
│   ├── 2_📚_常見學術寫作陷阱.py
│   ├── 3_📅_預約諮詢.py
│   └── 4_🏢_關於嵐海.py
├── lib/
│   └── footer.py                # 全站法律免責
├── .streamlit/config.toml
├── requirements.txt
└── runtime.txt
```

## 啟動

```bash
streamlit run app.py
```

## 內容撰寫鐵律

1. 全站不出現特定學校、地點、職稱、個人經歷
2. 顧問僅以「**楊念慈・論文陪跑專業顧問**」掛名，不寫個人學經歷
3. 公司資訊只露：公司名 + 聯絡 email（b0915905438@gmail.com） + LINE（pulovemo）
4. 案例敘事一律用「W 同學（碩士生）」「研究團隊整理」等去識別化寫法
5. 服務說明書、合約、倫理守則的內部版本由公司內部維護，網站只露要點

## 待辦

- [ ] 楊念慈個人介紹卡的最終措辭
- [ ] LOGO 與 favicon
- [ ] Calendly 連結（預約諮詢頁，目前用 form 收集）
- [ ] W2：lit-writer-lite 免費 demo
- [ ] W3：paper-reviewer-lite 免費 demo
