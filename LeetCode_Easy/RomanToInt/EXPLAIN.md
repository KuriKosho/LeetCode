# Chuyển Đổi Số La Mã Thành Số Nguyên Trong Python

## Bài Toán
Số La Mã được đại diện bởi bảy ký hiệu khác nhau:

| Ký hiệu | Giá trị |
|---------|---------|
| I       | 1       |
| V       | 5       |
| X       | 10      |
| L       | 50      |
| C       | 100     |
| D       | 500     |
| M       | 1000    |

Các số La Mã thường được viết từ lớn đến nhỏ từ trái sang phải. Tuy nhiên, có sáu trường hợp đặc biệt khi phải dùng phép trừ thay vì phép cộng:
- `I` đứng trước `V` hoặc `X` để tạo ra số 4 và 9.
- `X` đứng trước `L` hoặc `C` để tạo ra số 40 và 90.
- `C` đứng trước `D` hoặc `M` để tạo ra số 400 và 900.

**Ví dụ:**
- `III` = 3
- `LVIII` = 58
- `MCMXCIV` = 1994

## Phương Pháp Giải Quyết

Chúng ta sẽ thực hiện chuyển đổi một chuỗi số La Mã thành số nguyên bằng cách:
1. Tạo một bảng ánh xạ giữa các ký tự số La Mã và giá trị của chúng.
2. Duyệt qua từng ký tự trong chuỗi:

- Chúng ta sử dụng vòng lặp for để duyệt qua từng ký tự trong chuỗi:

- Nếu ký tự hiện tại (s[i]) có giá trị nhỏ hơn ký tự kế tiếp (s[i + 1]), điều này có nghĩa rằng ký tự hiện tại thuộc một trong các trường hợp đặc biệt (IV, IX, XL, XC, CD, CM), và chúng ta sẽ trừ giá trị của ký tự hiện tại từ tổng.
- Ngược lại, nếu ký tự hiện tại không thuộc các trường hợp đặc biệt, chúng ta cộng giá trị của nó vào tổng.
3. Kết quả cuối cùng là tổng của các giá trị đã xử lý.

## Mã Python

```python
def romanToInt(s: str) -> int:
    # Bảng ánh xạ giữa ký hiệu số La Mã và giá trị của chúng
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Khởi tạo tổng kết quả là 0
    total = 0
    # Duyệt qua từng ký tự trong chuỗi
    for i in range(len(s)):
        # Nếu ký tự hiện tại nhỏ hơn ký tự kế tiếp, trừ giá trị của ký tự hiện tại
        if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            total -= roman_to_int[s[i]]
        else:
            # Nếu không, cộng giá trị của ký tự hiện tại vào tổng
            total += roman_to_int[s[i]]
    
    return total
