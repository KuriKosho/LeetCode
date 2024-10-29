def merge(nums1, m, nums2, n):
    # Các con trỏ cho nums1, nums2 và cuối mảng đã hợp nhất
    i, j, k = m - 1, n - 1, m + n - 1

    # Hợp nhất theo thứ tự ngược
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Nếu còn bất kỳ phần tử nào trong nums2, sao chép chúng
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# Ví dụ sử dụng:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Đầu ra: [1, 2, 2, 3, 5, 6]