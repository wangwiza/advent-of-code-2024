def print_queue():

    page_ordering = {}
    updates = []

    with open('input.txt') as f:
        # parse page ordering rules
        for line in f:
            if line == '\n':
                break
            x, y = line.strip().split('|')
            x, y = int(x), int(y)
            if x not in page_ordering:
                page_ordering[x] = set([y])
            else:
                page_ordering[x].add(y)

        # parse pages in updates
        for line in f:
            updates.append([int(x) for x in line.strip().split(',')])
    
    def verify_update(update):
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[i] in page_ordering.get(update[j], []):
                    return False
        return True

    ans = 0
    # verify each update
    for update in updates:
        if verify_update(update):
            ans += update[len(update)//2]
    return ans

def print_queue2():
    
    page_ordering = {}
    updates = []

    with open('input.txt') as f:
        # parse page ordering rules
        for line in f:
            if line == '\n':
                break
            x, y = line.strip().split('|')
            x, y = int(x), int(y)
            if x not in page_ordering:
                page_ordering[x] = set([y])
            else:
                page_ordering[x].add(y)

        # parse pages in updates
        for line in f:
            updates.append([int(x) for x in line.strip().split(',')])
    
    def verify_update(update):
        b = True
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[i] in page_ordering.get(update[j], []):
                    update[i], update[j] = update[j], update[i]
                    b = False
        return b, update[len(update)//2]

    ans = 0
    # verify each update
    for update in updates:
        b, mid = verify_update(update)
        if not b:
            ans += mid
    return ans


if __name__ == "__main__":
    print(print_queue())
    print(print_queue2())
