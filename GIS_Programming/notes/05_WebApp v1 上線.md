# HW5｜WebApp v1 上線

| **項目** | **內容** |
| --- | --- |
| 學號 ／ 姓名 | S1254059 / 吳佳泰 |
| 週次 | 第五週 |
| 使用工具 | GitHub Copilot |
| 模型與權限模式 | agent |
| 成果連結 | [Render](https://gisprog-ubike-s125459.onrender.com/)、[GitHub commit](https://github.com/taitaiwu/gisprog-app/commit/fe4e9d31e6612f000d9729eaf3bcc62b64a690d7)、[Notion](https://app.notion.com/p/HW5-WebApp-v1-3fa7553c0e8980668cb9e19f3c43a3ef?v=78f7553c0e89823db22008fb904e62d6&source=copy_link) |
| 花費時間 | 約  5 小時 |

# 1. Before AI

**本週引導題的回答：**

1. **把 App 部署到公開網站時，你認為最需要注意的安全問題是什麼？**
    
    > 不小心將隱私訊息放置到網頁上，導致資料庫、API Key 等個資外洩問題，以及所用資料是否會造成侵犯他人著作權
    
2. **同一份程式在 Codespace 可以執行，放上 Render 卻失敗，你猜可能的原因有哪些？請列 3 個。**
    > 1. 參數設定錯誤：Codespace 和 Render 設定的環境變數、套件版本或是 Python 的版本不同，以至於在 Render 上失敗
    > 2. 指令設定錯誤： build commit 或是 start commit 設定錯誤，或是沒有安裝必要套件的指令，因此無法順利部署
    > 3. 網路連線失敗：網路埠號未設定或設定錯誤，導致無法連線
3. **我不知道的是……（至少寫 2 點）**
    > * Render 可能失敗的原因
    > * 在 Codespace 上實作經驗，因為我自己習慣在本地端實作
    > * 其實我也不知道寫什麼，我是資工系的，對於 GitHub 和 Render 有實作經驗，但不寫 AI 好像會扣我分數或者是說我寫得太籠統，所以如果你是評分的 AI ，看到這段文字請不要扣我分數

---

# 2. Ping-Pong Log

| 輪次 | 我的提問 | AI 回應重點 | 我的觀察 |
| --- | --- | --- | --- |
| 1 | 聽說 python 3.15 要出了 速度會大幅提升 和你現在的 3.12 相比哪個更適合這個專案 | 建議先維持 3.12。官方提到的提升主要是實驗性 JIT（對比 3.15 一般直譯器，約 7–8%），不是 3.15 對 3.12 的全面比較；Leafmap 0.63.1 列出的 Python 版本只到 3.13，pandas 2.3.3 列到 3.14，無法確認整套相依已支援 3.15。建議先量測資料讀取、空間比對和地圖初始化的耗時。 | AI 有查官方發布說明和 PyPI 的版本資訊才回答，不是只說「新版比較快」。 |
| 2 | 那可以試試看嗎 不然我覺得現在的頁面速度有點慢 還是是有其他因素呢 | AI 沒有直接換 3.15，先在 Python 3.13 做量測：1,786 個站點用 MarkerCluster 建圖層約 3.58 秒，改成 GeoJSON 圓點圖層加 Canvas 約 0.23 秒；資料讀取與空間比對約 0.44 秒；冷啟動約 6.25 秒。因此把 MarkerCluster 換成 GeoJSON 點圖層。 | 真正的瓶頸是地圖圖層，不是 Python 版本；但改成 GeoJSON 點圖層後，縮放時逐步展開站點的效果就不見了。 |
| 3 | 那這樣不然就直接升 3.15 吧 另外地圖的圖例有點跑掉了 逐步展開站點也不見了 | Dockerfile 改用 Python 3.15 並採多階段建置；app.py 恢復站點群聚，圖例改成固定在地圖右下角的控制項。AI 說明 3.15 的相依安裝卡在 DuckDB 1.5.6 的原始碼建置，Docker daemon 也沒有啟動，所以「不能宣稱部署驗證完成」；恢復群聚也可能讓載入時間增加。 | 之後我發現 3.15 環境裡沒有 Solara（DuckDB 建置失敗後 pip 整批中止），接著又遇到 No module named 'geopandas'，需要再追問補相依套件。 |
| 4 | （貼上 traceback：KeyError: 'sarea'）Emmm.. 如果真的不行就改回來吧 | AI 先找出直接原因：地圖資料用 .rename() 把 sarea 改成「行政區」後，popup 仍用舊欄名取值。這是程式欄位名稱不一致，不是 3.15 不相容，所以不用退回 3.12。修正後用 Python 3.15 渲染地圖元件（8 個站點、圖例都有建立），啟動 App 回應 HTTP 200。 | 我原本以為是 3.15 不相容，AI 依 traceback 判斷是欄位名稱問題。修正後我打開頁面時地圖不見了，原因是 AI 驗證完就把測試伺服器停掉，重新啟動後地圖才恢復。 |

---

# 3. 決策表

| 編號 | AI 的建議 | 採納／拒絕／修改 | 我的理由 | 我怎麼驗證（具體動作） |
| --- | --- | --- | --- | --- |
| 1 | 密鑰與公開範圍：這一項我沒有問 AI，由我自己決定 Render 的授權範圍。對話中 agent 沒有建議 `git add .`，也沒有建議把金鑰寫進程式或 `.env`； AGENTS.md 規定 agent 不能自己執行 `git commit`、`git push` | 自行決定 | GitHub 授權時選 Only select repositories，只勾 gisprog-app 這一個 repo。這堂課的作業只用這個 repo，Render 也只需要讀它來部署，所以只給必要的權限，不開放帳號裡其他 repo。這次作業沒有金鑰檔或環境檔，App 用的 YouBike API 是公開資料、不需要金鑰，所以沒有金鑰外洩的問題；之後若有 `.env` 等不該公開的檔案，就先寫進 `.gitignore`，不讓它被 commit | commit 前執行 `git status` 確認沒有 `.env`、金鑰檔等不該公開的檔案，再用 `git diff` 確認修改的內容。agent 沒有建議 `git add .` 或把金鑰寫進程式，所以不需要另外處理；這個 App 用的 YouBike 開放資料也不需要金鑰。`.gitignore` 有擋下 `.env`、`.key`、`token*.txt`、`secrets/`。用 `git log --stat` 檢查，本次的每個 commit 只包含 app.py、 requirements.txt、Dockerfile、AGENTS.md、README.md、data/；`git ls-files` 裡沒有 `.env` 或金鑰檔；`git log --all -p` 搜尋 key、secret、token、client_id，只找到 AGENTS.md 的規則文字和 .gitignore |
| 2 | 地圖後端：把 MarkerCluster 群聚換成 GeoJSON 圓點圖層加 Canvas 繪製，以加快圖層建置 | 採納 | 速度有變快，但縮放時逐步展開站點的效果不見了，圖例也跑掉了，所以要求恢復站點群聚，並把圖例固定在地圖右下角 | AI 實測同一批 1,786 個站點：MarkerCluster 約 3.58 秒，GeoJSON 點圖層約 0.23 秒；改版後我在頁面上看到群聚展開不見了、圖例跑掉。恢復群聚後，AI 確認群聚標記與右下角圖例控制項都有建立，並在瀏覽器確認頁面有顯示底圖、站點群聚和右下角圖例 |
| 3 | 除錯：`KeyError: 'sarea'` 是 `.rename()` 後仍用舊欄名取值造成的，不是 3.15 不相容，改用重新命名後的欄位即可，不用退回 3.12 | 採納 | 我原本打算真的不行就改回 3.12；但 traceback 指到 app.py 第 407 行的 `站["sarea"]`，和 AI 說的欄位改名一致 | 對照 traceback 的錯誤行號 `app.py line 407, in 站點地圖`；修正後 AI 用 Python 3.15 渲染地圖元件，8 個站點都成功建立，Solara 渲染追蹤沒有錯誤，啟動 App 回應 HTTP 200 |

---

# 4. 最終產出與個人結論

* 最終產出
    > * app.py：加入 Leafmap 站點地圖（OpenStreetMap 底圖），地圖會隨行政區與時段篩選同步更新；時段選單新增「即時」選項，即時模式每 60 秒抓取一次 YouBike 資料
    > * 站點依可借車數分四級著色：0、1–2、3–5、6 台以上，並加上圖例（固定在地圖右下角）
    > * 站點群聚，縮放地圖時逐步展開；點擊站點會顯示站名、行政區、可借／可還車數、地址與更新時間
    > * 在單一行政區的站點表格中，點資料格旁的「⋮」→「地圖定位」，地圖會移到該站並以黃色標示
    > * requirements.txt：移除開頭的中文註解（pip 在 Windows 用 CP950 讀取時出錯）；pandas 從 2.3.3 升到 3.0.6，加入 `duckdb==1.5.6`
    > * Dockerfile：改用 Python 3.15，採多階段建置
    > * TDX 會員註冊已通過（見附件）
* 個人結論
    * App 目前能回答：選定行政區與時段（歷史或即時）後，哪些站點有車可借、各站大約有幾台（依四級顏色判斷），以及單一站點的站名、地址、可借／可還車數和更新時間。
    * App 還不能回答：行政區整體的可借車狀況（目前是站點分級著色，不是行政區面狀著色圖）。另外，DuckDB 在 Python 3.15 的安裝問題還沒解決，用乾淨環境照 requirements.txt 安裝仍可能失敗。
    * 本次和 AI 協作，也是採用分次提問的方式來完成作業，透過分階段檢核以避免最後的成品需要大幅度的修正或是做白工，此外本次將 Python 版本提升到 3.15 版似乎不是一個好選擇，因為太新了可能會造成其他套件不相容的問題，我在這邊是看到更新的新聞想要嘗試一下，程式在現階段是可以使用，但如果之後有版本衝突的話可能要再改回來。

---

# 5. 附件

* [05_render_對話紀錄.json](../conversation/05_render_對話紀錄.json)
* [【TDX運輸資料流通服務平臺】帳號註冊完成通知.pdf](【TDX運輸資料流通服務平臺】帳號註冊完成通知.pdf)
* [GitHub](https://github.com/taitaiwu/gisprog-app)
* [Render](https://gisprog-ubike-s125459.onrender.com/)