def longest_substring(s, k):
    """
    This function uses a sliding window approach with two pointers.
    The idea is to keep expanding the right end of the window and when the window contains more than k distinct characters,
    start shrinking the left side of the window.
    """
    if not s or k == 0:
        return 0

    left, right = 0, 0
    max_length = 1
    char_frequency = {}

    while right < len(s):
        char_frequency[s[right]] = char_frequency.get(s[right], 0) + 1
        while len(char_frequency) > k:
            char_frequency[s[left]] -= 1
            if char_frequency[s[left]] == 0:
                del char_frequency[s[left]]
            left += 1
        max_length = max(max_length, right-left+1)
        right += 1

    return max_length

s = "aa"
k = 1
print(longest_substring(s, k))  # Outputs: 2
