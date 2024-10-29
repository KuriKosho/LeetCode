def mySqrt(x):
    # Khởi tạo giới hạn tìm kiếm nhị phân
    left, right = 0, x

    # Vòng lặp tìm kiếm nhị phân
    while left <= right:
        mid = (left + right) // 2
        # Kiểm tra nếu mid là căn bậc hai của x
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    # Trả về số nguyên lớn nhất nhỏ hơn hoặc bằng căn bậc hai
    return right

# Test case
print(mySqrt(4)) # 2
print(mySqrt(8)) # 2
print(mySqrt(9)) # 3
print(mySqrt(10)) # 3
print(mySqrt(16)) # 4
print(mySqrt(25)) # 5
print(mySqrt(100)) # 10