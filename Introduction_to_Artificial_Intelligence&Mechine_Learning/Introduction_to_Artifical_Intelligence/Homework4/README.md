# Homework4: Support Vector Machines

## Problem
你受聘為一家名叫 FutureBank 的資料分析實習生。FutureBank 最近有點慘，每個月都有客戶突然關帳戶，或是轉去別家銀行。主管開會氣到拍桌：「到底是誰把我們客戶都氣跑的！」而你作為新進的資料實習生，被指派成「客戶流失偵探」。主管丟給你一份神祕的檔案說：「這裡有客戶的資料，你幫我找出哪些人最有可能要落跑的！」你小心翼翼問：「那...我們要怎麼知道誰會跑？」主管皺眉：「你不是在修人工智慧嗎？SVM 什麼的都學過吧？」你想一想：「對耶」於是你從從容容遊刃有餘，準備開始進行一場「拯救銀行」的任務。

## Dataset
* 本資料集的任務是根據客戶的個人與銀行帳戶資料，預測該客戶是否會流失。請從作業區下載資料集，檔案格式皆為 `.csv` ，第一行是 column 名稱，第二行開始則是每一位客戶的資料。
* 內容包含三個 split： train, test, validation（validation以下簡稱 val）：
    * `train.csv`、`train_gt.csv` － train split 的 input 與 ground truth：3200筆
    * `val.csv`、`val_gt.csv` － val split 的 input 與 ground truth：400筆
    * `test.csv` － test split 的 input：400筆
* 每個 column 的資料種類具體如下：
    | 欄位名稱            | 類型     | 說明                               |
    | --------------- | ------ | -------------------------------- |
    | RowNumber       | int    | 資料編號                             |
    | CustomerId      | int    | 客戶編號                             |
    | Surname         | string | 客戶姓氏                             |
    | CreditScore     | int    | 信用評分（數值越高代表信用越好）                 |
    | Geography       | string | 客戶所在國家（France / Spain / Germany） |
    | Gender          | string | 性別（Male / Female）                |
    | Age             | int    | 年齡                               |
    | Tenure          | int    | 客戶在銀行的年資（單位：年）                   |
    | Balance         | float  | 銀行帳戶餘額                           |
    | NumOfProducts   | int    | 使用的銀行產品數                         |
    | HasCrCard       | int    | 是否擁有信用卡（1：有，0：無）                 |
    | IsActiveMember  | int    | 是否為活躍客戶（1：活躍，0：非活躍）              |
    | EstimatedSalary | float  | 客戶估計年薪                           |
    | Exited          | int    | 目標變數：是否流失（1：流失，0：未流失）            |


## Assignment Description
* 本次作業請使用 Python 3 完成。
* 本次作業請使用 Python 中 Machine Learning 開源套件：scikit-learn (sklearn)
* 提供的 Support Vector Machine SVM 來完成你的預測結果，套件下載指令如下：
    ```
    pip install scikit-learn
    ```
* 本次作業分為五個步驟：
    1. 了解資料
        * 下載資料集，理解題目的意義。
        * 參閱上述的 column 定義，也可以分析與統計各個 column 的資料，思考如何處理。
    2. 前處理
        * 由於有不同種的資料，在進行後續的模型預測之前，需要先將各種資料進行前處理，例如轉換成模型可以運算的型別、做資料視覺化幫助分析等等。
        * 可以嘗試設計不同的前處理方式，來達到更高的準確度。
    3. 建立與訓練模型
        * 按照課堂上所學，應用 Support Vector Machine，以 training set 訓練，再對 validation set 與 testing set 進行預測。Hw4 Support Vector Machine2
    4. 評估與優化
        * 利用 validation set 進行預測與評分，想辦法提升準確度，例如調整模型的參數或是嘗試加上特殊的前處理方式。
        * 我們有提供評估程式碼 `eval.py` ，使用方法範例如下，假設輸出的預測結果為`val_pred.csv` ，對應 `val_gt.csv` 為答案，則計算 `validation set` 準確率的指令：
            ```
            python eval.py val_gt.csv val_pred.csv
            ```
    5. 輸出預測結果
        * 請將 validation set `val.csv` 與 testing set `test.csv` 的預測結果分別儲存成 `val_pred.csv` 與 `test_pred.csv` 兩個 csv 檔。
        * 格式的部分，第一行固定是 `Exited` ，第二行開始是按照順序的預測結果 (1=流失 或 0=未流失)，如下方範例(4筆資料)：
            ```bash
            Exited
            1
            0
            0
            1
            ```
    6.  撰寫心得報告
        * 請根據作業檔案中提供的 report.docx 進行撰寫與修改。
        * 報告內容如下
            * 資料前處理做法說明
                * 你使用了什麼樣的前處理方式
                * 資料視覺化圖表
                * 最後挑選了哪些欄位作為輸入
            * SVM 模型選擇說明
                * 怎麼挑選 SVM 的參數？
                * 為甚麼這樣挑選參數的效果會比較好或比較不好？
                * 比較兩種以上不同參數的 SVM 帶來的結果，並說明模型產生不同結果的原因
# Notice
* 請使用 Python 3 完成作業，版本 $\geq$ 3.8。
* 撰寫程式碼，變數命名必須有意義、須包含註解。
* **嚴禁抄襲，我們會使用比對工具檢查！**

## Submission
* 本次作業需要繳交以下檔案：
    * svm.py－ SVM 程式碼
    * val_pred.csv － 對 val.csv 的預測結果
    * test_pred.csv － 對 test.csv 的預測結果
    * report.docx (或 report.pdf)－ 本次的作業報告

> 💡 我們只有提供 validation set 的答案讓同學測試，而 testing set 是隱藏測資