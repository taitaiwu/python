# 作業三：AES 加密系統的雪崩效應量化分析

## 實驗目標
驗證 AES 演算法的 **擴散（Diffusion）** 特性。透過計算「明文改變 1 bit」與「密文改變 bit 總數」的關係，理解為何微小的輸入差異會導致不可預測的輸出結果，從而對抗差異分析（Differential Cryptanalysis）。

## 實驗環境與工具
學生可自由選擇以下工具之一：
* 指令列工具：如 `OpenSSL`。
* 程式語言庫：如 Python (`PyCryptodome`)、Java (`javax.crypto`)。
* 線上工具：需支援 16 進位（Hex）輸出與手動輸入 Key/IV。

## 實驗步驟與輸入
1. 建立基準組
    1. 金鑰 (Key)：固定使用 `000102030405060708090a0b0c0d0e0f` (128-bit)。
    2. 初始向量 (IV)：固定使用 `00000000000000000000000000000000` (適用於 CBC/CTR 模式)。
    3. 原始明文 ($P_1$)：使用 `00000000000000000000000000000000` (128-bit Hex)。
    4. 執行加密：記錄產生的密文 $C_1$ 。

2. 建立對照組（改變 1-bit）
    1. 修改明文 ($P_2$)：將 $P_1$ 的最後一個位元改變。
        * 例如：將最後兩位從 `00` 改為 `01`（這代表改變了最後 1 個 bit）。
    2. 執行加密：使用相同的金鑰與 IV 對 $P_2$ 進行加密，記錄密文 $C_2$ 。

3. 量化計算
    1. 將 $C_1$ 與 $C_2$ 轉換為二進位（Binary）格式。
    2. 逐位元比對兩者的差異數量（即計算 Hamming Distance）。

## 輸出要求（實驗報告內容）
學生需提交一份簡要報告，包含以下數據：
* 密文紀錄：
    * $C_1$ (Hex): `________________`
    * $C_2$ (Hex): `________________`
* 差異位元數 (Bit Flip Count)：$C_1$ 與 $C_2$ 之間有多少 bits 不同？
* 改變率 (Percentage)： $\text{改變率} =\frac{\text{差異位元數}}{128} \times 100\%$
* 分析討論：
    * 根據你的實驗結果，改變率是否接近 50% ？這代表什麼意義？
    * 如果加密演算法沒有展現出良好的雪崩效應（例如改變率僅 5%），對安全性會有什麼威脅？

---

# 實驗報告

## 實驗紀錄
```
[Test 1]
P1: 00000000000000000000000000000000
P2: 00000000000000000000000000000001
C1: c6a13b37878f5b826f4f8162a1c8d879
C2: 7346139595c0b41e497bbde365f42d0a
Bit differences: 64
Percentage: 50.00%
[Test 2]
P1: 0123456789abcdeffedcba9876543210
P2: 0023456789abcdeffedcba9876543210
C1: 868d79bd49a5681cfae908ad51300ba0
C2: 074a710c58ea6daaf73a19124671b0cd
Bit differences: 60
Percentage: 46.88%
[Test 3]
P1: 0e3634aece7225b6f26b174ed92b5588
P2: 0f3634aece7225b6f26b174ed92b5588
C1: 1604bb9d63c2bb40354cc74a86585410
C2: a720f2e89b15974722d0dcc6159210da
Bit differences: 60
Percentage: 46.88%
[Test 4]
P1: 657470750fc7ff3fc0e8e8ca4dd02a9c
P2: c4a9ad090fc7ff3fc0e8e8ca4dd02a9c
C1: b43c998985aa139aef388294bbd1582c
C2: 829f0b1a280389ab3a7d642455f42143
Bit differences: 67
Percentage: 52.34%
[Test 5]
P1: 5c7bb49a6b72349b05a2317ff46d1294
P2: fe2ae569f7ee8bb8c1f5a2bb37ef53d5
C1: 7dfe1f0c20c59339ee270a5e54fc3ed1
C2: b0b311802f8c122b9eabd62fae62196a
Bit differences: 62
Percentage: 48.44%
[Test 6]
P1: 7115262448dc747e5cdac7227da9bd9c
P2: ec093dfb7c45343d689017507d485e62
C1: fb25c203fa456001df99bd2d2171345c
C2: f3962a28e95270cc7fd5af36c378ccbc
Bit differences: 52
Percentage: 40.62%
[Test 7]
P1: f867aee8b437a5210c24c1974cffeabc
P2: 43efdb697244df808e8d9364ee0ae6f5
C1: facd7c2246b4f4efae6a1ea9bd3ebf55
C2: 7bcc2e802b62089217ff2f344f2641e8
Bit differences: 68
Percentage: 53.12%
[Test 8]
P1: 721eb200ba06206dcbd4bce704fa654e
P2: 7b28a5d5ed643287e006c099bb375302
C1: c6a144c109b230057ee30f543048d4a0
C2: 0ac200daa6a74a3e0685f24b4621d329
Bit differences: 68
Percentage: 53.12%
[Test 9]
P1: 0ad9d85689f9f77be1c5f71185e5fb14
P2: 3bce2d8b6798d8ac4fe36a1d891ac181
C1: a3e2dc9da04b0ad0c0192472299c611b
C2: 716aa259864ee43f0296b39cec1783b7
Bit differences: 68
Percentage: 53.12%
[Test 10]
P1: db18a8ffa16d30d5f788b08d777ba4ea
P2: 9fb8b5452023c70280e5c4bb9e555a4b
C1: 975447b4d44f724039439e2898989dfb
C2: 729171e026ffcdf48ccae7685c5bd5f7
Bit differences: 60
Percentage: 46.88%
[Test 11]
P1: f91b4fbfe934c9bf8f2f85812b084989
P2: 20264e1126b219aef7feb3f9b2d6de40
C1: cc00b04299efd6cd330a967a0d5441df
C2: 5a87245e6306a25371a7380029b363bc
Bit differences: 65
Percentage: 50.78%
[Test 12]
P1: cca104a13e678500ff59025f3bafaa34
P2: b56a0341b2290ba7dfdfbddcd8578205
C1: 37bbff7db7dd559515c2895caeeb28bc
C2: 1654dabd5fad1774292cc9356171b197
Bit differences: 60
Percentage: 46.88%
[Test 13]
P1: ff0b844a0853bf7c6934ab4364148fb9
P2: 612b89398d0600cde116227ce72433f0
C1: fd934dc42ed784011ad2fbf0664ef51f
C2: 0adde2bf8042da45de16f60cac092d04
Bit differences: 70
Percentage: 54.69%
```

## 分析討論
1. **根據你的實驗結果，改變率是否接近 50% ？這代表什麼意義？**
    > Ans：是，幾乎都落在40%~60%區間，很接近理論值，代表具有良好的雪崩效應

2. **如果加密演算法沒有展現出良好的雪崩效應（例如改變率僅 5%），對安全性會有什麼威脅？**
    > Ans：可能會有跡可尋，攻擊者可以推測哪些 bit 影響哪些輸出，藉此破密
