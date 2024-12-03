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
    return any([check_ascending(levels[:i]+levels[i+1:]) for i in range(len(levels))])

def check_descending_dampened(levels):
    return any([check_descending(levels[:i]+levels[i+1:]) for i in range(len(levels))])

def count_safe_reports():
    with open('input.txt') as f:
        ans = 0
        for report in f:
            levels = [int(x) for x in report.split()]
            if not check_ascending(levels) and not check_descending(levels):
                continue
            ans += 1
    return ans

def count_dampened_safe_reports():
    with open('input.txt') as f:
        ans = 0
        for report in f:
            levels = [int(x) for x in report.split()]
            if not check_ascending_dampened(levels) and not check_descending_dampened(levels):
                continue
            ans += 1
    return ans

if __name__ == '__main__':
    print(count_safe_reports())
    print(count_dampened_safe_reports())
    