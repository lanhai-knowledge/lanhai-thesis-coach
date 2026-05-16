# 嵐海知識｜維運手冊

> 給未來的自己。記錄需要登入第三方後台、不能寫進 git 的設定步驟。

## 預約諮詢信件 SMTP 設定

> 對應檔案：[lib/mailer.py](lib/mailer.py)、[pages/3_📅_預約諮詢.py](pages/3_📅_預約諮詢.py)、[.streamlit/secrets.toml.example](.streamlit/secrets.toml.example)
> 首次設定日：2026-05-02

### 為什麼這樣設計

- **Gmail SMTP 而不是 Resend / SendGrid / Formspree**：個人陪跑業務一天頂多幾封信，Gmail 免費額度（500 封/日）綽綽有餘；不用註冊新服務、不用改 DNS、不用付月費。
- **From = To = `lanlanio1103@gmail.com`**：自己寄給自己 deliverability 最高，不會被 Gmail 標 spam。Reply-To 才是預約者 email，Gmail 按「回覆」就直接回到客戶信箱。
- **Secrets 走 Streamlit Cloud 後台**：本機 `.streamlit/secrets.toml` 已被 `.gitignore` 排除；正式 secrets 只活在 Streamlit Cloud，repo 從不接觸到密碼。

### Step 1：申請 Gmail App Password

App Password 是 Google 給「會用 SMTP 登入的程式」用的 16 碼一次性密碼，**不是** Gmail 登入密碼。

1. 用 `lanlanio1103@gmail.com` 登入 Google 帳戶
2. 開啟兩階段驗證（前置條件，沒開無法申請 App Password）
   - https://myaccount.google.com/security
   - 找「兩步驟驗證」→ 啟用
3. 申請 App Password
   - https://myaccount.google.com/apppasswords
   - 應用程式名稱填「嵐海預約系統」（任意，自己看得懂即可）
   - 點「建立」→ 跳出 16 碼密碼（含空格，例：`abcd efgh ijkl mnop`）
   - **這個密碼只顯示一次，立刻複製**

> 找不到 App Password 入口？通常是兩階段驗證沒開。
> 撤銷舊密碼？同樣在 https://myaccount.google.com/apppasswords 可以管理。

### Step 2：在 Streamlit Cloud 後台設 Secrets

1. 進 https://share.streamlit.io/
2. 找到 `lanhai-thesis-coach` app → 右上 `︙` → **Settings**
3. 左側選 **Secrets** 分頁
4. 在文字框貼上以下內容（把 `SMTP_PASS` 換成 Step 1 拿到的 16 碼）：

   ```toml
   SMTP_HOST = "smtp.gmail.com"
   SMTP_PORT = 465
   SMTP_USER = "lanlanio1103@gmail.com"
   SMTP_PASS = "abcd efgh ijkl mnop"
   BOOKING_TO = "lanlanio1103@gmail.com"
   ```

5. 按 **Save**
6. App 會自動 reboot（約 30 秒～1 分鐘），底部 log 會跑一次重啟流程

> 收件人想加多人？把 `BOOKING_TO` 寫成 `"a@gmail.com, b@gmail.com"`，逗號分隔。

### Step 3：驗收（一定要做）

1. 打開 https://lanhai-thesis-coach.streamlit.app/預約諮詢
2. 填一筆測試資料：
   - 稱呼：`測試-(今天日期)`
   - Email：填自己另一個信箱（這樣可測 Reply-To 是否正確）
   - 主題、痛點隨便填一句
   - 勾選同意條款
3. 按「送出預約」
4. 預期看到綠字「✅ 預約資訊已寄出」
5. 30 秒內到 `lanlanio1103@gmail.com` 收件匣確認：
   - 主旨格式：`【嵐海預約】測試-XXXX｜尚未決定，希望初談後再評估`
   - 內文是純文字、欄位齊全
   - 在 Gmail 按「回覆」→ To 自動帶到你 Step 2 填的另一個信箱（不是 lanlanio1103）

### 萬一壞掉

| 症狀 | 可能原因 | 怎麼查 |
|---|---|---|
| 紅字「缺少 secrets：SMTP_USER」 | Streamlit Cloud secrets 沒存到 / app 還沒 reboot 完 | 回 Settings → Secrets 確認文字框內容；左下重新整理 app |
| 紅字「SMTPAuthenticationError」 | Gmail App Password 錯 / 兩階段驗證被關掉 | 重新申請 App Password、確認帳戶仍開兩階段 |
| 送出後綠字成功但收不到信 | Gmail 把自己寄給自己丟到「促銷內容」或「垃圾郵件」 | 全信箱搜尋「嵐海預約」；找到後右鍵「永不寄到垃圾郵件」 |
| Streamlit log 出現 `timeout` | Streamlit Cloud 偶發網路問題 | 重試一次；若連續壞 1 小時以上去 https://www.streamlitstatus.com/ 看 |

### 想換成別的寄信服務時看這裡

如果哪天量大到 Gmail 擋（一天 500 封以上），或想要更專業的 deliverability 報表：

- **Resend**（推薦）：3000 封/月免費，要設 DNS 驗證 domain，API key 取代 SMTP
- **SendGrid**：100 封/日免費，老牌但 UI 較重
- **Mailgun**：5000 封/月前 3 個月免費，之後付費

換的話只要改 `lib/mailer.py` 一個檔，pages/ 不用動。
