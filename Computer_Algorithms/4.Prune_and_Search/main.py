def prune_and_search(n: int, list1: list[float]) -> float:
    if (n <= 5):
        for i in range(1, n):
            temp = list1[i]
            j = i - 1

            while (j >= 0 and list1[j][0] > temp[0]):
                list1[j+1] = list1[j]
                j -= 1

            list1[j+1] = temp

        w_total = sum(w for x, w in list1)
        add = 0

        for x, w in list1:
            add += w

            if (add >= w_total / 2):
                return x
            
        return list1[-1][0]
    
    else:
        median = []

        for i in range(0, n, 5):  #horizontal sorting
            line = list1[i:min(i+5, n)]

            for j in range(1, len(line)):
                temp = line[j]
                k = j - 1

                while (k >= 0 and line[k][0] > temp[0]):
                    line[k+1] = line[k]
                    k -= 1

                line[k+1] = temp

            median.append(line[len(line)//2][0])

        for i in range(1, len(median)):  #medians sorting
            temp = median[i]
            j = i - 1

            while (j >= 0 and median[j] > temp):
                median[j+1] = median[j]
                j -= 1

            median[j+1] = temp


        mid_midian = median[len(median)//2]

        s1 = [(x, w) for x, w in list1 if (x < mid_midian)]
        s2 = [(x, w) for x, w in list1 if (x == mid_midian)]
        s3 = [(x, w) for x, w in list1 if (x > mid_midian)]

        w_s1 = sum(w for x, w in s1)
        w_s2 = sum(w for x, w in s2)
        w_s3 = sum(w for x, w in s3)

        w_total = w_s1 + w_s2 + w_s3

        if (w_total / 2 < w_s1):
            return prune_and_search(len(s1), s1)
        
        elif (w_total / 2 <= w_s1 + w_s2):
            return mid_midian
        
        else:
            return prune_and_search(len(s3), s3)


n = int(input())
list1 = []

for i in range(n):
    temp = input().split()
    list1.append([float(i) for i in temp])

m = prune_and_search(n, list1.copy())
goal = sum(w * abs(m-x) for x, w in list1)

print(m)
print(goal)