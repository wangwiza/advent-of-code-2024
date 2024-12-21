from collections import Counter

def plutonian_pebbles():
    with open('input.txt') as f:
        stones = list(map(int,f.read().strip().split()))
    for _ in range(25): # blink 25 times
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
                i += 1
            elif (l:=len(str(stones[i]))) % 2 == 0:
                stones[i] = str(stones[i])
                stones[i:i+1] = [int(stones[i][:l//2]), int(stones[i][l//2:])]
                i += 2
            else:
                stones[i] = stones[i]*2024
                i += 1
    return len(stones)

def plutonian_pebbles2():
    with open('input.txt') as f:
        stones = list(map(int,f.read().strip().split()))
    d = Counter(stones)
    for _ in range(75): # blink 25 times
        nd = {}
        for stone, freq in d.items():
            if stone == 0:
                nd[1] = nd.get(1,0) + freq
            elif (l:=len(str(stone))) % 2 == 0:
                first = int(str(stone)[:l//2])
                second = int(str(stone)[l//2:])
                nd[first] = nd.get(first,0) + freq
                nd[second] = nd.get(second,0) + freq
            else:
                nd[stone*2024] = nd.get(stone*2024, 0) + freq
        d = nd
    return sum(d.values())


if __name__ == '__main__':
    print(plutonian_pebbles())
    print(plutonian_pebbles2())
