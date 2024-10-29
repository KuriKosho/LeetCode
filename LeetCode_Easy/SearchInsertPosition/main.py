def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Tìm thấy target tại chỉ mục mid
        elif nums[mid] < target:
            left = mid + 1  # Tìm kiếm phía phải
        else:
            right = mid - 1  # Tìm kiếm phía trái
    return left  # left là vị trí cần chèn target nếu không tìm thấy

# Test
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Kết quả 2