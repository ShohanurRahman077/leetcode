from collections import defaultdict
def longestSubstringWithoutRepeating(s):
    count = defaultdict(int)
    left = 0
    ans = 0
    for i in range(len(s)):
        count[s[i]] +=1
        while count[s[i]] >1:
            count[s[left]] -=1
            left +=1
            
            
        ans  = max(ans, i - left +1)
    return (ans)


longestSubstringWithoutRepeating("abcabcbb")