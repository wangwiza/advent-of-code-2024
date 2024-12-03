def check_ascending(levels):
    for i in range(1, len(levels)):
        if not 1 <= levels[i] - levels[i-1] <= 3 :
            return False
    return True

def check_descending(levels):
    for i in range(1, len(levels)):
        if not 1 <= levels[i-1] - levels[i] <= 3 :
            return False
    return True

def check_ascending_dampened(levels):
    dampened = False
    for i in range(1, len(levels)):
        if not 1 <= levels[i] - levels[i-1] <= 3 :
            if not dampened:
                dampened = True
                continue
            return False
    return True

def check_descending_dampened(levels):
    dampened = False
    for i in range(1, len(levels)):
        if not 1 <= levels[i-1] - levels[i] <= 3 :
            if not dampened:
                dampened = True
                continue
            return False
    return True

def count_safe_reports():
    with open('input.txt') as f:
        ans = 0
        for report in f:
            levels = [int(x) for x in report.split()]
            if len(levels) <= 1:
                ans += 1
                continue
            if levels[0] < levels[1]: # increasing
                if not check_ascending(levels):
                    continue
                ans += 1
            if levels[0] > levels[1]: # decreasing
                if not check_descending(levels):
                    continue
                ans += 1
    return ans

def count_dampened_safe_reports():
    with open('input.txt') as f:
        ans = 0
        for report in f:
            levels = [int(x) for x in report.split()]
            if len(levels) <= 1:
                ans += 1
                continue
            if levels[0] < levels[1]: # increasing
                if not check_ascending_dampened(levels):
                    continue
                ans += 1
            if levels[0] > levels[1]: # decreasing
                if not check_descending_dampened(levels):
                    continue
                ans += 1
    return ans

if __name__ == '__main__':
    print(count_safe_reports())
    print(count_dampened_safe_reports())
    