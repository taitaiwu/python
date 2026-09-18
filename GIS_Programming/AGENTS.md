# 115-1 地理資訊系統運用程式：課程專案規範（給 AI Coding Agent）

## 專案背景

- 這是彰師大地理系「地理資訊系統運用程式」的課程資料夾，使用者是正在學習 Python 與 GIS 程式設計的大學部學生。
- notebook 主要在 **Google Colab** 執行。本資料夾透過 Google 雲端硬碟電腦版同步到本機，讓 agent 讀寫檔案。

## 資料夾結構

- `data/raw/`：原始資料。**唯讀：禁止修改、覆寫、刪除、移動或重新命名。**
- `data/processed/`：清理後的資料。
- `notebooks/`：Jupyter notebook。檔名以兩位數週次開頭，例如 `01_first_look.ipynb`。
- `outputs/`：圖表與結果表。
- `fonts/`：中文字型，由 `00_Colab環境設定範本.ipynb` 自動下載。

## 程式撰寫規則

1. 新 notebook 的第一個程式儲存格，必須沿用 `notebooks/00_Colab環境設定範本.ipynb` 的路徑設定，用 `RAW_DIR`、`PROCESSED_DIR`、`OUTPUT_DIR` 組合路徑。**禁止寫死本機路徑**，例如 `G:\...` 或 `C:\Users\...`。
2. 程式必須能在 Google Colab 執行。優先使用 Colab 內建套件；需要其他套件時，先說明理由並取得我的同意，再用 `%pip install` 寫進 notebook。
3. 註解與 Markdown 說明一律使用繁體中文（台灣用語）。
4. 以初學者看得懂為原則：一個儲存格只做一件事，避免過長的鏈式呼叫。
5. 要輸出給 Excel 開啟的 CSV，使用 `encoding="utf-8-sig"`。
6. **API 金鑰、token、密碼不得寫進程式碼或 notebook。** 需要時用 Colab 的 Secrets（`google.colab.userdata`）讀取。

## 資料判讀原則

- 資料來源寫在 `data/raw/資料來源說明.md`。
- 不要只憑欄位名稱猜測欄位的意義、單位或統計範圍。請先實際檢查資料內容，必要時查資料來源的官方說明，再列出你的判斷與依據；不確定時直接說不確定。

## 協作方式

- 新增或修改檔案前，先簡述計畫，並列出會動到哪些檔案。
- 執行安裝套件、刪除檔案或其他 shell 指令前，先說明這個指令做什麼。
- 提出建議時附上理由，讓我能判斷要採納、拒絕或修改。
- 我在 Colab 開著某份 notebook 時，請不要同時修改那份檔案。
