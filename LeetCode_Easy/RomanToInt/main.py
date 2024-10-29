def romanToInt(s: str) -> int:
    # Define a dictionary to map Roman symbols to their integer values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the total result to 0
    total = 0
    # Iterate over the string, looking at each character and the one after it
    for i in range(len(s)):
        # If the current character has a smaller value than the next character, subtract it
        if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            total -= roman_to_int[s[i]]
        else:
            # Otherwise, add it to the total
            total += roman_to_int[s[i]]

    return total

# Test cases
print(romanToInt("III"))  # 3
print(romanToInt("IV"))   # 4