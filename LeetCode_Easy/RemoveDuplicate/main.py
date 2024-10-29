def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0  # Pointer for the last unique element found

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # Fill the remaining elements with underscores (optional, only for display purposes)
    for k in range(i + 1, len(nums)):
        nums[k] = '_'

    return i + 1

# test cases
nums = [1, 1, 2]
print(removeDuplicates(nums))  # 2
print(nums)  # [1, 2, '_']