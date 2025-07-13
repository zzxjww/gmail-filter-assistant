import streamlit as st
import json
import pandas as pd
import os

# 載入假資料
def load_emails(path="sample_emails.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# 儲存標記結果
def save_labels(labeled_data, save_path="labeled_emails.csv"):
    df = pd.DataFrame(labeled_data)
    df.to_csv(save_path, index=False, encoding="utf-8-sig")

# 初始化
st.set_page_config(page_title="Gmail 郵件分類助手", layout="centered")
st.title("📬 Gmail 郵件分類 Demo")
emails = load_emails()
labeled_results = []

# 顯示每封信
for i, email in enumerate(emails):
    with st.expander(f"📩 {email['subject']} (From: {email['sender']})"):
        st.write(email["body"])
        label = st.selectbox(
            f"選擇標籤 (信件 {i+1})",
            ["未分類", "工作", "社交", "廣告", "垃圾", "其他"],
            key=f"label_{i}"
        )
        labeled_results.append({
            "sender": email["sender"],
            "subject": email["subject"],
            "body": email["body"],
            "label": label
        })

# 儲存按鈕
if st.button("💾 儲存所有標記結果"):
    save_labels(labeled_results)
    st.success("已成功儲存到 labeled_emails.csv！")