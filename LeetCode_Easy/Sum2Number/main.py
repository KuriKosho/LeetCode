def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
    return None

nums = [3,3,2,4]
target = 7
print(two_sum(nums, target))