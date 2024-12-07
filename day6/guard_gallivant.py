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

    def is_out_of_bounds(x,y):
        return x < 0 or x >= h or y < 0 or y >= w

    def has_obstacle_in_front(x,y,dir_i):
        x += directions[dir_i][0]
        y += directions[dir_i][1]
        if is_out_of_bounds(x,y):
            return False
        return map[x][y] == '#'

    # main loop
    while not is_out_of_bounds(x,y):
        # if on top of obstacle, backtrack and change direction
        if has_obstacle_in_front(x,y,dir_i):
            dir_i = (dir_i + 1) % 4
        else:
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
    
    # vars
    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    for i in range(h):
            for j in range(w):
                if map[i][j] == '^':
                    initial_x, initial_y = i, j
                    break
    def is_out_of_bounds(x,y):
        return x < 0 or x >= h or y < 0 or y >= w

    def has_obstacle_in_front(x,y,dir_i):
        x += directions[dir_i][0]
        y += directions[dir_i][1]
        if is_out_of_bounds(x,y):
            return False
        return map[x][y] == '#'
            

    def check_infinite_loop():
        dir_i = 0
        visited = set()
        x, y = initial_x, initial_y
        while not is_out_of_bounds(x,y):
            if has_obstacle_in_front(x, y, dir_i):
                if (x, y, dir_i) in visited:
                    return True
                visited.add((x, y, dir_i))
                dir_i = (dir_i + 1) % 4
            else:
                x += directions[dir_i][0]
                y += directions[dir_i][1]
        return False

    def get_guard_path():
        path = []
        x, y = initial_x, initial_y
        dir_i = 0
        while not is_out_of_bounds(x,y):
            path.append((x,y))
            # if on top of obstacle, backtrack and change direction
            if has_obstacle_in_front(x,y,dir_i):
                dir_i = (dir_i + 1) % 4
            else:
                x += directions[dir_i][0]
                y += directions[dir_i][1]
        return path
    
    possible_cells = set(get_guard_path()[1:])

    ans = set()
    for x, y in possible_cells:
        map[x][y] = '#'
        if check_infinite_loop():
            ans.add((x,y))
        map[x][y] = '.'
    return len(ans)

if __name__ == '__main__':
    print(guard_gallivant())
    print(guard_gallivant2())
