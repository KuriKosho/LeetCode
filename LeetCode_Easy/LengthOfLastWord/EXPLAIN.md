# Bài Toán: Tìm Độ Dài Từ Cuối Trong Chuỗi

Cho chuỗi `s` bao gồm các từ và dấu cách, hãy trả về độ dài của từ cuối cùng trong chuỗi.

- Một từ là chuỗi ký tự liên tiếp không có dấu cách.
- Đảm bảo rằng sẽ có ít nhất một từ trong chuỗi.

### Ví Dụ

1. **Input**: `s = "Hello World"`  
   **Output**: `5`  
   **Giải Thích**: Từ cuối là "World" với độ dài `5`.

2. **Input**: `s = "   fly me   to   the moon  "`  
   **Output**: `4`  
   **Giải Thích**: Từ cuối là "moon" với độ dài `4`.

3. **Input**: `s = "luffy is still joyboy"`  
   **Output**: `6`  
   **Giải Thích**: Từ cuối là "joyboy" với độ dài `6`.

### Ràng Buộc

- `s` chỉ chứa các chữ cái tiếng Anh và khoảng trắng `' '`.
- Chuỗi có ít nhất một từ.

## Hướng Giải Quyết

1. **Sử Dụng `split()`**:
   - Dùng hàm `split()` để tách các từ trong chuỗi `s` thành một danh sách các từ.
   - Phần tử cuối cùng trong danh sách sẽ là từ cuối cùng trong chuỗi.
   - Trả về độ dài của phần tử cuối cùng này.

2. **Duyệt Từ Cuối Chuỗi (Không Dùng `split()`)**:
   - Bỏ qua các khoảng trắng ở cuối chuỗi (nếu có).
   - Bắt đầu từ ký tự cuối cùng và đếm ngược để tìm từ cuối cùng.
   - Khi gặp khoảng trắng tiếp theo, dừng đếm và trả về độ dài của từ.

### Mã Python

#### Phương Pháp Dùng `split()`

```python
def lengthOfLastWord(s):
    words = s.split()
    return len(words[-1])  # Từ cuối cùng
```

#### Phương Pháp duyệt cuối mảng

```python
def lengthOfLastWord(s):
    n = len(s)
    i = n - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    count = 0
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1
    return count
```

