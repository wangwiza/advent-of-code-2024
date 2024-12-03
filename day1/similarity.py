from collections import Counter

l1 = []
l2 = []
with open('input.txt') as f:
    for line in f:
        x1, x2 = line.split()
        l1.append(int(x1))
        l2.append(int(x2))


d = Counter(l2)
print(sum([x*d[x] for x in l1]))

# d1 = {}
# d2 = {}
# sum = 0
# with open('input.txt') as f:
#     for line in f:
#         x, y = line.split()
#         d1[x] = d1.get(x, 0) + 1
#         d2[y] = d2.get(y, 0) + 1
#         sum += 
