# Bài Toán Leo Cầu Thang

Bạn đang leo một cầu thang. Cần `n` bước để lên đỉnh. Mỗi lần bạn có thể leo 1 hoặc 2 bước. Có bao nhiêu cách khác nhau để bạn leo lên đỉnh?

## Câu Truy Vấn

- **Ví dụ 1:**
    - **Đầu vào:** `n = 2`
    - **Đầu ra:** `2`
    - **Giải thích:** Có hai cách để leo lên đỉnh.
        1. 1 bước + 1 bước
        2. 2 bước

- **Ví dụ 2:**
    - **Đầu vào:** `n = 3`
    - **Đầu ra:** `3`
    - **Giải thích:** Có ba cách để leo lên đỉnh.
        1. 1 bước + 1 bước + 1 bước
        2. 1 bước + 2 bước
        3. 2 bước + 1 bước

## Giới Hạn

- `1 <= n <= 45`

## Giải Thích

1. **Hiểu Vấn Đề**:
   - Bạn có thể đến bậc `n` từ bậc `(n-1)` (bằng cách đi 1 bước) hoặc từ bậc `(n-2)` (bằng cách đi 2 bước).
   - Điều này có nghĩa là tổng số cách khác nhau để đến bậc `n` là tổng số cách để đến bậc `(n-1)` và bậc `(n-2)`.

2. **Định Nghĩa Đệ Quy**:
   - Gọi `f(n)` là số cách khác nhau để đến bậc `n`.
   - Mối quan hệ có thể được diễn đạt như sau:
     \[
     f(n) = f(n-1) + f(n-2)
     \]
   - Các trường hợp cơ sở:
     - `f(1) = 1` (1 cách để leo 1 bước)
     - `f(2) = 2` (2 cách để leo 2 bước)

3. **Cách Tiếp Cận Lập Trình Động**:
   - Chúng ta có thể sử dụng một mảng để lưu trữ số cách để đến mỗi bậc cho đến `n`.
   - Khởi tạo hai bậc đầu tiên và tính toán số cách cho mỗi bậc cho đến `n`.

4. **Mối Quan Hệ Fibonacci**:
   - Bài toán này tương đương với việc tìm số Fibonacci thứ `n+1` nếu chúng ta bắt đầu chuỗi Fibonacci với `F(1) = 1`, `F(2) = 1`, và tiếp tục.

## Cài Đặt

Dưới đây là cách bạn có thể cài đặt giải pháp trong Python:

```python
def climbStairs(n):
    # Các trường hợp cơ sở
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Khởi tạo hai bậc đầu tiên
    a, b = 1, 2

    # Tính số cách cho mỗi bậc từ 3 đến n
    for i in range(3, n + 1):
        a, b = b, a + b  # a là f(n-2), b là f(n-1)

    return b  # f(n) được lưu trữ trong b

# Ví dụ sử dụng:
print(climbStairs(2))  # Đầu ra: 2
print(climbStairs(3))  # Đầu ra: 3
