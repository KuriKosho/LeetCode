## Kiểm tra số đối xứng (Palindrome) mà không chuyển số thành chuỗi

Để kiểm tra xem một số nguyên `x` có phải là **số đối xứng** (palindrome) hay không, chúng ta cần xem liệu số đó có giống nhau khi đọc từ trái sang phải và từ phải sang trái.

### Ý tưởng

1. **Số âm không phải là palindrome**: Vì chúng có dấu trừ `-` ở đầu, nên chúng không thể đối xứng. Ví dụ: `-121` không thể đối xứng.
2. **Số có chữ số cuối là 0 (trừ số 0)**: Nếu `x` có chữ số cuối là `0`, nó cũng không phải là palindrome, vì số đối xứng sẽ có chữ số đầu là `0`, điều này không hợp lệ (số không có chữ số thừa ở đầu).
3. **So sánh nửa đầu và nửa cuối**: 
   - Để kiểm tra đối xứng, chỉ cần kiểm tra nửa đầu và nửa cuối của số.
   - Ta có thể lấy nửa cuối của số bằng cách **đảo ngược một nửa** số `x`.
   - Nếu `x` bằng nửa cuối đã đảo ngược hoặc `x` bằng nửa cuối đã đảo ngược bỏ đi chữ số cuối, thì `x` là palindrome.

### Giải thuật

1. Loại trừ các trường hợp đặc biệt: nếu `x < 0` hoặc `x` có chữ số cuối là `0` (và `x` không phải là `0`), trả về `false`.
2. Tạo một biến `reversed_half` để lưu trữ nửa cuối đã đảo ngược của `x`.
3. Lặp lại đến khi `x` nhỏ hơn hoặc bằng `reversed_half`:
   - Cập nhật `reversed_half` bằng `reversed_half * 10 + x % 10` (lấy chữ số cuối của `x` và thêm vào `reversed_half`).
   - Giảm `x` xuống còn một chữ số bằng `x // 10`.
4. Sau khi thoát khỏi vòng lặp, kiểm tra:
   - Nếu `x` bằng `reversed_half` hoặc `x` bằng `reversed_half // 10`, trả về `true`.
   - Ngược lại, trả về `false`.

### Code Python

```python
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
