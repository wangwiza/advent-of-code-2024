def ceres_search():
    # get input 2D array
    arr = []
    with open("input.txt") as f:
        for line in f:
            arr.append(list(line[:-1]))

    h = len(arr)
    w = len(arr[0])

    ans = 0
    mas = 'MAS'

    def direction_has_xmas(x, y, direction):
        for i in range(3):
            x += direction[0]
            y += direction[1]
            if x < 0 or x >= h or y < 0 or y >= w or arr[x][y] != mas[i]:
                return False
        return True


    for x in range(h):
        for y in range(w):
            if arr[x][y] == 'X':
                for direction in [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]:
                    if direction_has_xmas(x, y, direction):
                        ans += 1
    return ans

def ceres_search2():
    # get input 2D array
    arr = []
    with open("input.txt") as f:
        for line in f:
            arr.append(list(line[:-1]))
    h = len(arr)
    w = len(arr[0])
    ans = 0
    def is_xmas(x,y):
        if arr[x][y] != 'A':
            return False
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            return False
        d1 = (arr[x-1][y-1] == 'M' and arr[x+1][y+1] == 'S') or (arr[x-1][y-1] == 'S' and arr[x+1][y+1] == 'M')
        d2 = (arr[x-1][y+1] == 'M' and arr[x+1][y-1] == 'S') or (arr[x-1][y+1] == 'S' and arr[x+1][y-1] == 'M')
        return d1 and d2

    for x in range(h):
        for y in range(w):
            if is_xmas(x, y):
                ans += 1
    return ans

    


if __name__ == "__main__":
    print(ceres_search())
    print(ceres_search2())
