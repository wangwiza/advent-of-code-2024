def resonant_collinearity():
    # build map
    map = []
    with open('input.txt') as f:
        for line in f:
            map.append(list(line.strip()))
    h = len(map)
    w = len(map[0])

    # find antennas and antinodes
    
    def is_in_map(x,y):
        return 0 <= x < h and 0 <= y < w
    
    antinodes = set()
    antennas = {}
    
    for i in range(h):
        for j in range(w):
            v = map[i][j]
            if v == '.': # equivalent to is not alnum
                continue

            if v not in antennas: # can't create antinode with one antenna
                antennas[v] = [(i,j)]
            else: # have seen another antenna of same frequency
                for x,y in antennas[v]:
                    # (i,j) and (x,y)
                    dx, dy = i-x, j-y # (dx, dy)
                    # (i,j) + (dx,dy) and (x,y) - (dx, dy)
                    if is_in_map(i+dx, j+dy):
                        antinodes.add((i+dx,j+dy))
                    if is_in_map(x-dx,y-dy):
                        antinodes.add((x-dx,y-dy))
                antennas[v].append((i,j))
    return len(antinodes)

def resonant_collinearity2():
    # build map
    map = []
    with open('input.txt') as f:
        for line in f:
            map.append(list(line.strip()))
    h = len(map)
    w = len(map[0])

    # find antennas and antinodes
    
    def is_in_map(x,y):
        return 0 <= x < h and 0 <= y < w
    
    antinodes = set()
    antennas = {}
    
    for i in range(h):
        for j in range(w):
            v = map[i][j]
            if v == '.': # equivalent to is not alnum
                continue

            if v not in antennas: # can't create antinode with one antenna
                antennas[v] = [(i,j)]
            else: # have seen another antenna of same frequency
                for x,y in antennas[v]:
                    a = 0
                    dx, dy = i-x, j-y # the slope
                    # loop for "harmonics"
                    while is_in_map(nx:=i+a*dx, ny:=j+a*dy):
                        antinodes.add((nx,ny))
                        a += 1
                    a = 0
                    while is_in_map(nx:=x-a*dx, ny:=y-a*dy):
                        antinodes.add((nx,ny))
                        a += 1
                antennas[v].append((i,j))
    return len(antinodes)


if __name__ == '__main__':
    print(resonant_collinearity())
    print(resonant_collinearity2())
