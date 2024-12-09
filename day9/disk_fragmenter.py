
def disk_fragmenter_attempt():
    with open('input.txt') as f:
        disk_map = list(map(int, f.read().strip()))

    front = 0
    back = len(disk_map)-1
    compact = ""
    while front < back-1:
        # print(front, back, disk_map)
        if front % 2 == 0: # front is on file-block
            compact += str(front//2)*disk_map[front] # append front file
            front += 1
        elif disk_map[front] >= disk_map[back]: # enough free space
            compact += str(back//2)*disk_map[back] # append back file
            disk_map[front] -= disk_map[back] # consumed front space
            back -= 2 # go to next back file
        else: # not enough free space
            compact += str(back//2)*(disk_map[front])
            disk_map[back] -= disk_map[front] # consumed back file
            front += 1
    compact += str(back//2)*disk_map[back]
    checksum = 0
    for i, v in enumerate(compact):
        checksum += i*int(v)
    return checksum

def disk_fragmenter():
    with open('input.txt') as f:
        disk_map = list(map(int, f.read().strip()))
    
    expanded = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            expanded += [str(i//2)]*disk_map[i]
        else:
            expanded += ['.']*disk_map[i]
    i = 0
    while i < len(expanded):
        if expanded[i] != '.':
            i += 1
            continue
        while (v:=expanded.pop()) == '.':
            pass
        expanded[i] = v
        i += 1
    return sum(i*int(v) for i,v in enumerate(expanded))

def disk_fragmenter2():
    with open('input.txt') as f:
        disk_map = list(map(int, f.read().strip()))
    
    expanded = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            expanded += [str(i//2)]*disk_map[i]
        else:
            expanded += ['.']*disk_map[i]
    i = 0
    while i < len(expanded):
        if expanded[i] != '.':
            i += 1
            continue
        while (v:=expanded.pop()) == '.':
            pass
        expanded[i] = v
        i += 1
    return sum(i*int(v) for i,v in enumerate(expanded))


if __name__ == '__main__':
    print(disk_fragmenter())
    print(disk_fragmenter2())
