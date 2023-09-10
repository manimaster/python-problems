def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for word in word_dict:
            if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True

    return dp[-1]
