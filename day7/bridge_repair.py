def can_operate_to_target(nums, target) -> bool:
    def backtrack(acc, i) -> bool:
        if i == len(nums):
            return acc == target
        return backtrack(acc + nums[i], i + 1) or backtrack(acc * nums[i], i + 1)
    return backtrack(0,0)

def can_operate_to_target2(nums, target) -> bool:
    def backtrack(acc, i) -> bool:
        if i == len(nums):
            return acc == target
        return backtrack(acc + nums[i], i + 1) or backtrack(acc * nums[i], i + 1) or backtrack(int(f"{acc}{nums[i]}"), i + 1)
    return backtrack(0,0)

def bridge_repair():
    ans = 0
    ans2 = 0
    with open('input.txt') as f:
        for line in f:
            target, nums = line.strip().split(':')
            target = int(target)
            nums = list(map(int, nums.split()))
            if can_operate_to_target(nums, target):
                ans += target
            if can_operate_to_target2(nums, target):
                ans2 += target
    return ans, ans2

if __name__ == '__main__':
    print(bridge_repair())
