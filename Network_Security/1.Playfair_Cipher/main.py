mode = input("Mode : ")
key = list(input("Key : ").replace(" ", ""))
text = list(input("Text : ").upper().replace(" ", ""))
key_matrix = []
counter1 = 0
counter2 = ord("A")
result = []

while (mode != "E" and mode != "e" and mode != "D" and mode != "d"):
    print("Mode Input error!!!")
    mode = input("Mode : ")

key = ["I" if (i == "J") else i for i in key]

for i in key:
    if (i not in key_matrix):
        key_matrix.append(i)
        counter1 += 1

while (counter1 < 25):
    if ((chr(counter2) not in key_matrix) and (chr(counter2) != "J")):
        key_matrix.append(chr(counter2))
        counter1 += 1
        
    counter2 += 1

if (mode == "E" or mode == "e"):
    i = 0
    j = len(text) - 1

    while (i < j):
        if (text[i] == text[i+1]):
            text.insert(i+1, "X")
            j += 1

        i += 2

    if (len(text) % 2 != 0):
        text.append("X")

    for i in range(0, len(text), 2):
        m = key_matrix.index(text[i])
        n = key_matrix.index(text[i+1])
        x1 = m % 5
        y1 = m // 5
        x2 = n % 5
        y2 = n // 5 
        
        if (x1 == x2):
            result.append([key_matrix[(m+5) % 25], key_matrix[(n+5) % 25]])
        
        elif (y1 == y2):
            result.append([key_matrix[5*y1 + (x1+1)%5], key_matrix[5*y2 + (x2+1)%5]])

        else:
            result.append([key_matrix[5 * y1 + x2], key_matrix[5 * y2 + x1]])

    answer = " ".join(["".join(i) for i in result])

elif (mode == "D" or mode == "d"):
    for i in range(0, len(text), 2):
        m = key_matrix.index(text[i])
        n = key_matrix.index(text[i+1])
        x1 = m % 5
        y1 = m // 5
        x2 = n % 5
        y2 = n // 5 
        

        if (x1 == x2):
            result.append(key_matrix[(m-5) % 25])
            result.append(key_matrix[(n-5) % 25])       
        
        elif (y1 == y2):
            result.append(key_matrix[5*y1 + (x1-1)%5])
            result.append(key_matrix[5*y2 + (x2-1)%5])

        else:
            result.append(key_matrix[5 * y1 + x2])
            result.append(key_matrix[5 * y2 + x1])

    counter1 = 0
    counter2 = len(result)
    while (counter1 < counter2):
        if (result[counter1] == "X"):
            if ((counter1 == counter2 - 1) or ((counter1 > 0) and (counter1 < counter2 - 1) and (result[counter1-1] == result[counter1+1]))):
                result.pop(counter1)
                counter2 -= 1

        counter1 += 1

    answer = "".join(result)


print("Key Matrix : ")
for i in range(len(key_matrix)):
    print(key_matrix[i], end=" ") 

    if ((i + 1) % 5 == 0):
        print(end="\n") 


print("\nResult :", answer)
