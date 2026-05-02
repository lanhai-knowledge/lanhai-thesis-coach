"""嵐海知識｜SMTP 寄信工具（Gmail App Password）"""

from __future__ import annotations
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from typing import Iterable

import streamlit as st


class MailerConfigError(RuntimeError):
    pass


def _get_secret(key: str) -> str:
    try:
        value = st.secrets[key]
    except (KeyError, FileNotFoundError, st.errors.StreamlitSecretNotFoundError):
        raise MailerConfigError(f"缺少 secrets：{key}")
    if not value:
        raise MailerConfigError(f"secrets {key} 為空值")
    return str(value)


def send_booking_email(
    *,
    subject: str,
    body: str,
    reply_to: str | None = None,
) -> None:
    """寄出一封預約通知信到嵐海收件信箱。

    Secrets 需要：
        SMTP_HOST（預設 smtp.gmail.com）
        SMTP_PORT（預設 465，SSL）
        SMTP_USER（Gmail 完整地址，例：b0915905438@gmail.com）
        SMTP_PASS（Gmail App Password 16 碼）
        BOOKING_TO（收件信箱，可逗號分隔多人）
    """
    host = st.secrets.get("SMTP_HOST", "smtp.gmail.com")
    port = int(st.secrets.get("SMTP_PORT", 465))
    user = _get_secret("SMTP_USER")
    password = _get_secret("SMTP_PASS")
    to_raw = _get_secret("BOOKING_TO")
    recipients: list[str] = [r.strip() for r in to_raw.split(",") if r.strip()]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = f"嵐海知識預約系統 <{user}>"
    msg["To"] = ", ".join(recipients)
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="lanhai-thesis-coach")
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context, timeout=20) as server:
        server.login(user, password)
        server.send_message(msg, from_addr=user, to_addrs=recipients)


def format_booking_body(fields: dict[str, object]) -> str:
    """把表單欄位整理成純文字信件內容。"""
    lines: list[str] = ["嵐海知識｜新預約通知", "=" * 40, ""]
    for label, value in fields.items():
        if isinstance(value, list):
            value = ", ".join(value) if value else "（未選）"
        if value in (None, ""):
            value = "（未填）"
        lines.append(f"【{label}】")
        lines.append(str(value))
        lines.append("")
    lines.append("=" * 40)
    lines.append("此信由 lanhai-thesis-coach.streamlit.app 自動寄出")
    return "\n".join(lines)
