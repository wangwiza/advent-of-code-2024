def hoof_it():
    with open('input.txt') as f:
        hike_map = [list(map(int, line.strip())) for line in f]
    h = len(hike_map)
    w = len(hike_map[0])

    def get_neighbours(x, y):
        return [(nx, ny) for nx, ny in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)] if 0 <= nx < h and 0 <= ny < w]

    summits = set()
    def backtrack(x, y, k):
        if k == 10:
            if (x,y) not in summits:
                summits.add((x,y))
                return 1
            else:
                return 0
        total = 0
        for nx, ny in get_neighbours(x, y):
            if hike_map[nx][ny] == k:
                total += backtrack(nx, ny, k+1)
        return total

    ans = 0
    for x in range(h):
        for y in range(w):
            if hike_map[x][y] == 0:
                summits = set()
                ans += backtrack(x,y,1)
    return ans

def hoof_it2():
    with open('input.txt') as f:
        hike_map = [list(map(int, line.strip())) for line in f]
    h = len(hike_map)
    w = len(hike_map[0])

    def get_neighbours(x, y):
        return [(nx, ny) for nx, ny in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)] if 0 <= nx < h and 0 <= ny < w]

    def backtrack(x, y, k):
        if k == 10:
            return 1
        total = 0
        for nx, ny in get_neighbours(x, y):
            if hike_map[nx][ny] == k:
                total += backtrack(nx, ny, k+1)
        return total

    ans = 0
    for x in range(h):
        for y in range(w):
            if hike_map[x][y] == 0:
                ans += backtrack(x,y,1)
    return ans


if __name__ == '__main__':
    print(hoof_it())
    print(hoof_it2())
