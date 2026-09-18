# 115-1_GISprog｜地理資訊系統運用程式 課程資料夾

## 放置位置

把整個 `115-1_GISprog` 資料夾放在 **Google 雲端硬碟「我的雲端硬碟」的最上層**，資料夾名稱不要更改。

在 Colab 裡，這個資料夾的路徑是 `/content/drive/MyDrive/115-1_GISprog`。

## 資料夾結構

| 位置 | 用途 |
|---|---|
| `AGENTS.md` | 給 AI agent 的課程規範（Codex、Copilot 讀取；Claude Code 透過 `CLAUDE.md` 匯入） |
| `CLAUDE.md` | Claude Code 的規範檔，內容匯入 `AGENTS.md` |
| `.claude/settings.json` | Claude Code 專案設定：預設為手動核准模式，並禁止編輯 `data/raw/` |
| `data/raw/` | 原始資料，**唯讀** |
| `data/processed/` | 清理後的資料 |
| `notebooks/` | Jupyter notebook，從 `00_Colab環境設定範本.ipynb` 開始 |
| `outputs/` | 圖表與結果表 |

`.claude` 是隱藏資料夾。在 Windows 檔案總管中看不到時，請到「檢視」→「顯示」→勾選「隱藏的項目」。

## 第一次使用

1. 在 Google 雲端硬碟中，對 `notebooks/00_Colab環境設定範本.ipynb` 按右鍵，選「開啟工具」→「Google Colaboratory」。
2. 依序執行每個儲存格。第一次執行時，會跳出 Google 帳號授權視窗，請同意存取雲端硬碟。
3. 最後一張長條圖的中文正常顯示，就代表環境設定完成。

## W4 之後

W4 起改用 GitHub repo 與 GitHub Codespaces 開發 Web App。這個 Drive 資料夾仍用於 Colab 探索分析。
