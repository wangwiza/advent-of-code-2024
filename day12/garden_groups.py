from collections import deque

def garden_groups():
    with open('input.txt') as f:
        garden_map = list(map(list, [line.strip() for line in f]))
    h = len(garden_map)
    w = len(garden_map[0])

    def get_neighbours(x,y,c):
        return [(nx,ny) for nx,ny in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)] if 0 <= nx < h and 0 <= ny < w and garden_map[nx][ny] == c]
    
    visited = set()

    def calculate_region_cost(x,y):
        area = 0
        perimeter = 0
        
        visited.add((x,y))
        # BFS
        q = deque([(x,y)])
        while q:
            cur = q.popleft()
            area += 1
            neighbours = get_neighbours(cur[0],cur[1],garden_map[cur[0]][cur[1]])
            perimeter += 4-len(neighbours)
            for neighbour in neighbours:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)
        return area * perimeter
            
    ans = 0
    for i in range(h):
        for j in range(w):
            if (i,j) not in visited:
                ans += calculate_region_cost(i,j)
    return ans

if __name__ == '__main__':
    print(garden_groups())
