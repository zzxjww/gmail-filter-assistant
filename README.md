# Gmail Filter Assistant

### 執行方式

#### 1. 建議建立虛擬環境

```bash
python -m venv .venv
source .venv/bin/activate      # 啟用虛擬環境
```

#### 2. 安裝套件

```bash
pip install -r requirements.txt
```

或如果沒成功的話

```bash
pip install streamlit pandas
```

#### 3. 啟動介面

在 frontend 資料夾裡面跑
`streamlit run app.py`

現在都只是很初步的一個介面之後應該會大大大大大修，所以參考看看就好

### 目前架構（待大大大大大修）

```plaintext
gmail-filter-assistant/
├── frontend/
│   ├── app.py               # 主程式：Streamlit 前端邏輯
│   ├── sample_emails.json   # 假資料：模擬 Gmail 郵件
│   ├── labeled_emails.csv   # 使用者標記後的結果（自動產生）
│   ├── utils.py             # 資料處理工具（可選、尚未）
│   ├── requirements.txt     # 套件清單
│   └── .gitignore
├── models/                  # 模型程式與預測邏輯
└── README.md
```
