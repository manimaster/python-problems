def min_window(s, t):
    from collections import Counter

    char_count = Counter(t)
    required_chars = len(t)
    l, r = 0, 0
    min_len = float('inf')
    min_str = ""

    while r < len(s):
        if char_count[s[r]] > 0:
            required_chars -= 1
        char_count[s[r]] -= 1

        while required_chars == 0:
            window_len = r - l + 1
            if window_len < min_len:
                min_len = window_len
                min_str = s[l:r+1]

            char_count[s[l]] += 1
            if char_count[s[l]] > 0:
                required_chars += 1
            l += 1
        r += 1

    return min_str
