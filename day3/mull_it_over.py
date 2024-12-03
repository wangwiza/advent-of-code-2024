import re

def mull_it_over():
    with open('input.txt') as f:
        ans = 0
        for match in re.finditer('mul\(([0-9]{1,3}),([0-9]{1,3})\)',f.read()):
            ans += int(match.group(1)) * int(match.group(2))
        return ans
    
def mull_it_over2():
    with open('input.txt') as f:
        ans = 0
        disabled = False
        for match in re.finditer('(mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don\'t\(\))',f.read()):
            if match.group(0) == "do()":
                disabled = False
            elif match.group(0) == "don't()":
                disabled = True
            elif not disabled:
                ans += int(match.group(2)) * int(match.group(3))
        return ans
    
if __name__ == '__main__':
    # print(mull_it_over())
    print(mull_it_over2())