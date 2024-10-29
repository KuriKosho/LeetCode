def removeElement(nums, val):
    n = len(nums) - 1  # Initialize the pointer for the last element
    i = 0
    while i <= n:
        if nums[i] == val:
            nums[i] = nums[n]  # Replace the element at i with the element at n
            n -= 1  # Shrink the size of the valid array
        else:
            i += 1  # Move to the next element if nums[i] is not val
    return n + 1  # The number of elements not equal to val

# Test cases
print(removeElement([3, 2, 2, 3], 3))  # 2