while True:
    try:
        n1, n2 = input().split()
        list1 = [[0 for _ in range(len(n1)+1)] for _ in range(len(n2)+1)]

        for i in range(1, len(n2)+1):
            for j in range(1, len(n1)+1):
                if (n1[j-1] == n2[i-1]):
                    temp = list1[i-1][j-1] * 10 + int(n1[j-1])
                    list1[i][j] = max(temp, list1[i-1][j], list1[i][j-1])
                else:
                    list1[i][j] = max(list1[i-1][j], list1[i][j-1])

        print(int(list1[len(n2)][len(n1)]))

    except EOFError:
        break