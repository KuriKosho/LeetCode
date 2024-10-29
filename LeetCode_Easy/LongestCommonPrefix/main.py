def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Khởi tạo tiền tố là chuỗi đầu tiên
    prefix = strs[0]

    # Duyệt qua từng chuỗi trong mảng
    for s in strs[1:]:
        # Cắt ngắn tiền tố nếu không khớp với chuỗi hiện tại
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Test case
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))  # Output: "fl"