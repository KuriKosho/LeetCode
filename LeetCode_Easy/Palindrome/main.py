def is_palindrome(x):
    # Trường hợp x là số âm hoặc số kết thúc bằng 0 nhưng không phải là 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    # Đảo ngược nửa số để so sánh
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Kiểm tra đối xứng
    return x == reversed_half or x == reversed_half // 10

# Test
print(is_palindrome(121)) # True