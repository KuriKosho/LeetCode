def plusOne(digits):
    # Duyệt ngược qua từng chữ số trong mảng
    for i in range(len(digits) - 1, -1, -1):
        # Nếu chữ số khác 9, tăng lên 1 và trả về mảng
        if digits[i] != 9:
            digits[i] += 1
            return digits
        # Nếu chữ số là 9, đặt thành 0 (carry)
        digits[i] = 0

    # Trường hợp tất cả các chữ số là 9, thêm 1 ở đầu mảng
    return [1] + digits

# Test cases
print(plusOne([1, 2, 3])) # [1, 2, 4]