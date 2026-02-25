def sift_down(x: list[float], i: int, n: int):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        max_num = i

        if ((left < n) and (x[left] > x[max_num])):
            max_num = left

        if ((right < n) and (x[right] > x[max_num])):
            max_num = right
            
        if (max_num == i):
            break

        x[max_num], x[i] = x[i], x[max_num]
        i = max_num

def heap_sort(x: list[float]):
    for i in range(len(x)//2 - 1, -1, -1):
        sift_down(x, i, len(x))

    for i in range(len(x) - 1, 0, -1):
        x[0], x[i] = x[i], x[0]
        sift_down(x, 0, i)

def rank_find(cood: list[list[float]]) -> int:
    if (len(cood) == 1):
        return [0] * len(cood)
    
    x = [i[0] for i in cood]
    heap_sort(x)
    median = x[len(x)//2] if (len(x)%2 != 0) else (x[len(x)//2] + x[len(x)//2 - 1])/2
    a = [i for i in cood if (i[0] < median)]
    b = [i for i in cood if (i[0] >= median)]

    rank_a = rank_find(a)
    rank_b = rank_find(b)
    
    
    for i, j in enumerate(b):
        for k in a:
            if k[1] <= j[1]:
                rank_b[i] += 1

    return rank_a + rank_b
    

f = open("test2.txt")
line = f.readline().replace("\n", "")
s = []

while line:
    s.append(line)
    line = f.readline().replace("\n", "")

f.close()

s = [[float(j) for j in i.split()] for i in s]
rank = rank_find(s)

x = [i[0] for i in s]
heap_sort(x)
s_dict = {a: b for a, b in s}

print("Homework2 - 2D Ranking")
print("---------------------------------------")
print()
print("X\tY\trank")
print("---------------------")
for i in range(len(x)):
    print(x[i], s_dict[x[i]], rank[i], sep="\t")

print()
print("(1) The number of all points :", len(s))
print("(2) Maximum rank :", max(rank))
print("(3) Minimum rank :", min(rank))
print("(4) Average rank : {:.2f}".format(sum(rank) / len(rank)))