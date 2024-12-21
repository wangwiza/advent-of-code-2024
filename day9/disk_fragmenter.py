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
    disk_list = []
    space_list = []
    file_list = []
    count = 0
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk_list += [str(i//2)]*disk_map[i]
            file_list.append((str(i//2),disk_map[i],count))
        else:
            disk_list += ['.']*disk_map[i]
            space_list.append((disk_map[i], count))
        count += disk_map[i]
    file_list = file_list[::-1] # reverse to start from biggest value file
    for file in file_list:
        for i in range(len(space_list)):
            if file[1] > space_list[i][0] or file[2] < space_list[i][1]:
                continue
            for j in range(space_list[i][1],space_list[i][1]+file[1]):
                disk_list[j] = file[0]
            for j in range(file[2],file[2]+file[1]):
                disk_list[j] = '.'
            if file[1] == space_list[i][0]:   
                space_list.pop(i)
            elif file[1] < space_list[i][0]:
                space_list[i] = (space_list[i][0]-file[1],space_list[i][1]+file[1])
            break
    return sum(i*int(file_id) for i, file_id in enumerate(disk_list) if file_id != '.')
            


if __name__ == '__main__':
    # print(disk_fragmenter())
    print(disk_fragmenter2())
