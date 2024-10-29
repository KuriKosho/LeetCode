def addBinary(a, b):
    # Khởi tạo các biến
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    # Lặp lại cho đến khi duyệt hết cả hai chuỗi
    while i >= 0 or j >= 0 or carry:
        # Lấy giá trị chữ số hiện tại của a và b, nếu có
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Tính tổng và cập nhật carry
        total = digit_a + digit_b + carry
        result.append(str(total % 2))  # Lưu chữ số vào kết quả
        carry = total // 2  # Cập nhật carry

        # Di chuyển con trỏ sang trái
        i -= 1
        j -= 1

    # Kết quả phải được đảo ngược vì chúng ta thêm vào từ cuối
    return ''.join(result[::-1])

# Test cases
print(addBinary("11", "1"))  # Expected: "100"