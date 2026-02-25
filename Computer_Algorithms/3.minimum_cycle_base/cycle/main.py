# all_cycle (rewrite from cycle.cpp)

fname = "cost239"

with open("cost239", "r") as fp: 
    newline = fp.readline().split() 
    nodenum = int(newline[0]) if (len(newline) > 1) else int(newline) 
    edgenum = int(newline[1]) if (len(newline) > 1) else 0
    A = [[0 for _ in range(nodenum)] for _ in range(nodenum)] # store connected points 
    
    while True: 
        line = fp.readline() 
        
        if not line: 
            break 
        
        if not line.strip(): 
            continue 
        
        begin, end, cost = map(int, line.strip().split()) 
        A[begin][end] = 1 
        A[end][begin] = 1


edge = []

for i in range(nodenum):
    for j in range(i + 1, nodenum):
        if (A[i][j]):
            edge.append((i, j))

edgenum = len(edge)

order = [[-1] * nodenum for _ in range(20000)] # default : -1
for i in range(nodenum):
    order[i][0] = i

b = 0  # There are b temps 
s = 0 
e = nodenum
cycle_paths = []
all_cycle_vectors = []

for no in range(1, nodenum):
    adde = 0
    s = 0

    for k in range(e):
        s += b
        b = 0
        pre = order[s][no - 1]  # pervious vector
        temp = []

        for i in range(pre + 1, nodenum):  # check repeat vector
            if A[pre][i] == 1:
                if i not in order[s][1:no]:
                    temp.append(i)

        b = len(temp)
        c = 0

        if (b > 0):
            adde += b - 1

            for i in range(e+adde, s, -1):  # e->e+adde
                for j in range(no):
                    order[i+b-1][j] = order[i][j]

            pre_path = order[s][:no]  # original path 

            for i in range(b):
                index = s + i
                order[index][:no] = pre_path[:]
                order[index][no] = temp[i]

                if ((no > 1) and (A[order[index][no]][order[index][0]] == 1)):  # check cycle
                    path = order[index][:no + 1]

                    seq1 = path[:]
                    seq2 = path[::-1]

                    def min_rotation(list1):
                        best = None
                        
                        for i in range(len(list1)):
                            a = tuple(list1[i:] + list1[:i])

                            if ((best is None) or (a < best)):
                                best = a

                        return best

                    min_seq1 = min_rotation(seq1)
                    min_seq2 = min_rotation(seq2)
                    outcome = min_seq1 if (min_seq1 <= min_seq2) else min_seq2

                    if outcome not in cycle_paths:
                        cycle_paths.append(outcome)
                        vec = [0] * edgenum  # convert to edge vectors
                        L = list(path)  # convert to list

                        for t in range(len(L)):
                            a = L[t]
                            b_node = L[(t + 1) % len(L)]

                            if (a < b_node):
                                pair = (a, b_node)

                            else:
                                pair = (b_node, a)

                            if pair in edge:
                                idx_edge = edge.index(pair)
                                vec[idx_edge] = 1

                        all_cycle_vectors.append(vec)

        else:
            for i in range(s, e+adde):
                for j in range(no+1):
                    order[i][j] = order[i + 1][j]

            adde -= 1

    e += adde


# minimum cycle basis  
vec_ints = []

for v in all_cycle_vectors:  # bitmask
    val = 0

    for bit in v:
        val = (val << 1) | (bit & 1)

    vec_ints.append(val)

idxs = sorted(range(len(vec_ints)), key=lambda i: (vec_ints[i].bit_count(), i))
min_cycle = []
min_cycle_int = []

for i in idxs:  # Gaussian elimination
    x = vec_ints[i]
    y = x

    for b in min_cycle_int:
        hb = b.bit_length() - 1
        if ((y >> hb) & 1):
            y ^= b

    if y != 0:
        min_cycle_int.append(y)
        min_cycle_int.sort(reverse=True)
        min_cycle.append(i)

print("Homework3 - minimum cycle base")
print("------------------------------\n")

for i in min_cycle:
    path = cycle_paths[i]
    print("->".join(map(str, path)) + "->" + str(path[0]))

print(len(min_cycle), "cycles(min)")
