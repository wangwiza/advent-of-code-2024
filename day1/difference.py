l1 = []
l2 = []
with open('input.txt') as f:
    for line in f:
        x1, x2 = line.split()
        l1.append(int(x1))
        l2.append(int(x2))
l1.sort()
l2.sort()
print(sum([abs(l1[i]-l2[i]) for i in range(len(l1))]))