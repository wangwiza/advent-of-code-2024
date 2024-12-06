def guard_gallivant():
    # obtain map
    map = []
    with open('input.txt') as f:
        for line in f:
            map.append(list(line.strip()))
    h = len(map)
    w = len(map[0])

    # find starting position
    for i in range(h):
        for j in range(w):
            if map[i][j] == '^':
                x, y = i, j
                break
    
    # vars
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    dir_i = 0
    ans = 0

    # main loop
    while 0 <= x < h and 0 <= y < w:
        # if on top of obstacle, backtrack and change direction
        if map[x][y] == '#':
            x -= directions[dir_i][0]
            y -= directions[dir_i][1]
            dir_i = (dir_i + 1) % 4
        # mark off current cell and count if not visited
        if map[x][y] != 'X':
            map[x][y] = 'X'
            ans += 1

        x += directions[dir_i][0]
        y += directions[dir_i][1]

    return ans

def guard_gallivant2():
    # obtain map
    map = []
    with open('input.txt') as f:
        for line in f:
            map.append(list(line.strip()))
    h = len(map)
    w = len(map[0])

    # find starting position
    for i in range(h):
        for j in range(w):
            if map[i][j] == '^':
                x, y = i, j
                break
    
    # vars
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    dir_i = 0
    ans = 0

    def check_if_loop(x, y, dir_i):
        visited = set()
        if (dir_i == 0 and y == 0) or (dir_i == 1 and x == 0) or (dir_i == 2 and y == w-1) or (dir_i == 3 and x == h-1):
            return False
        dir_i = (dir_i+1)%4
        cur_x, cur_y = x, y
        while 0 <= cur_x < h and 0 <= cur_y < w:
            if (cur_x, cur_y, dir_i) in visited:
                return True
            visited.add((cur_x, cur_y, dir_i))
            if map[cur_x][cur_y] == '#':
                cur_x -= directions[dir_i][0]
                cur_y -= directions[dir_i][1]
                dir_i = (dir_i + 1) % 4
                continue
            cur_x += directions[dir_i][0]
            cur_y += directions[dir_i][1]
        return False

    # main loop
    while 0 <= x < h and 0 <= y < w:
        # if on top of obstacle, backtrack and change direction
        if map[x][y] == '#':
            x -= directions[dir_i][0]
            y -= directions[dir_i][1]
            dir_i = (dir_i + 1) % 4
        elif check_if_loop(x, y, dir_i):
            # print(x+directions[dir_i][0], y+directions[dir_i][1])
            ans += 1

        x += directions[dir_i][0]
        y += directions[dir_i][1]
    return ans

if __name__ == '__main__':
    print(guard_gallivant())
    print(guard_gallivant2())
