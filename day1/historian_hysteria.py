from collections import Counter

def sum_of_distances():
    l1 = []
    l2 = []
    with open('input.txt') as f:
        for line in f:
            x1, x2 = line.split()
            l1.append(int(x1))
            l2.append(int(x2))
    l1.sort()
    l2.sort()
    return sum([abs(l1[i]-l2[i]) for i in range(len(l1))])

def sum_of_similarity_scores():
    l1 = []
    l2 = []
    with open('input.txt') as f:
        for line in f:
            x1, x2 = line.split()
            l1.append(int(x1))
            l2.append(int(x2))
    d = Counter(l2)
    return sum([x*d[x] for x in l1])

if __name__ == "__main__":
    print(sum_of_distances())
    print(sum_of_similarity_scores())