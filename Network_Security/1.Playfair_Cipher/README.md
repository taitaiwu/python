# 作業一：Playfair Cipher 加解密系統實作

## 題目描述
Playfair Cipher 是由 Charles Wheatstone 在 1854 年發明。它將明文兩兩一組（Digraphs），並根據一個 $5 \times 5$ 的金鑰矩陣進行轉換。本作業要求學生實作一個能夠處理**金鑰生成**、**加密**與**解密**的系統。

## 輸入格式 (Input Format)
輸入將包含三個部分：
1. 模式設定：`E` 代表加密（Encrypt），`D` 代表解密（Decrypt）。
2. 金鑰字串 (Key)：一個僅包含英文字母的字串（長度不限）。
3. 目標文本 (Text)：待處理的明文或密文。

> 字母處理規則：
> * 將 `J` 視為 `I` 處理。
> * 忽略空格與大小寫（統一轉為大寫）。

## 輸出格式 (Output Format)
1. 金鑰矩陣：輸出生成的 $5 \times 5$ 矩陣（用於除錯與評分）。
2. 結果文本：輸出加密或解密後的字串，每兩個字母一組（中間以空格隔開）。

## 作業要求與演算規則
學生必須嚴格遵循以下 Playfair 規則：
1. 矩陣建構
    * 使用金鑰字串填充矩陣。
    * 剩餘空間按 `A-Z` 順序填滿（跳過 `J`）。
2. 明文預處理（僅加密時）
    * 若兩兩分組時出現相同字母（如 `EE`），需在中間插入填充字（如 `X`），變成 `EX` `E`。
    * 若總長度為奇數，在末尾補一個 `X`。

## 範例展示
1. 輸入：
```
Mode: E
Key: PLAYFAIR EXAMPLE
Text: HIDE THE GOLD
```

2. 輸出：
```
Key Matrix:
P L A Y F
I R E X M
B C D G H
K N O Q S
T U V W Z

Result: BM OD ZB XD NA GE
```