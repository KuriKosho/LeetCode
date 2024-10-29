# Bài Toán: Tìm Chỉ Mục Đầu Tiên của Chuỗi Con trong Chuỗi Chính

Cho hai chuỗi ký tự `needle` và `haystack`, hãy trả về chỉ mục của lần xuất hiện đầu tiên của `needle` trong `haystack`. Nếu `needle` không nằm trong `haystack`, trả về `-1`.

### Yêu Cầu

1. Tìm vị trí xuất hiện đầu tiên của `needle` trong `haystack`.
2. Nếu không tìm thấy, trả về `-1`.

### Ví Dụ

1. **Input**: `haystack = "sadbutsad"`, `needle = "sad"`  
   **Output**: `0`  
   **Giải Thích**: Chuỗi "sad" xuất hiện ở chỉ mục `0` và `6`. Lần xuất hiện đầu tiên là tại `0`, nên trả về `0`.

2. **Input**: `haystack = "leetcode"`, `needle = "leeto"`  
   **Output**: `-1`  
   **Giải Thích**: "leeto" không xuất hiện trong "leetcode", nên trả về `-1`.

### Ràng Buộc

- `haystack` và `needle` chỉ gồm các chữ cái tiếng Anh thường.

## Hướng Giải Quyết

1. **Sử Dụng Hàm Tích Hợp `find()`**:
   - Hàm tích hợp `str.find(substring)` trong Python trả về chỉ mục của lần xuất hiện đầu tiên của chuỗi `substring` trong chuỗi chính `str`. Nếu không tìm thấy, nó trả về `-1`.
   - Đây là cách tối ưu và đơn giản nhất khi cần tìm chỉ mục của chuỗi con.

2. **Phương Pháp Duyệt Thủ Công**:
   - Với mỗi chỉ mục `i` từ `0` đến `len(haystack) - len(needle)`, so sánh `haystack[i:i + len(needle)]` với `needle`.
   - Nếu chuỗi con khớp với `needle`, trả về `i`. Nếu không tìm thấy, trả về `-1`.

### Mã Python

#### Phương Pháp Sử Dụng `find()`

```python
def strStr(haystack, needle):
    return haystack.find(needle)
```
#### Phương Pháp thủ công

```python
def strStr(haystack, needle):
    # Duyệt qua từng vị trí có thể trong haystack
    for i in range(len(haystack) - len(needle) + 1):
        # Kiểm tra xem đoạn chuỗi con có khớp needle không
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1
```
