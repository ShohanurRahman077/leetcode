from collections import defaultdict
def longestSubstringRepeatK(s,k):
    chars = defaultdict(int)
    left = right = 0

    res = 0
    while right < len(s):
        chars[s[right]] += 1
        print(chars)
        while chars[s[right]] >= k:
            chars[s[left]] -= 1
            left += 1
            res = max(res, right - left + 1)

        right += 1
    return res


print(longestSubstringRepeatK("ababbc",2))