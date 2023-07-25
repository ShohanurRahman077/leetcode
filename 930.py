from collections import Counter
def numOfSubArrayWithSum(nums, goal):
    P = [0]
    for x in nums: P.append(P[-1] + x)
    count = Counter()
    print(P)
    ans = 0
    for x in P:
        ans += count[x]
        count[x + goal] += 1
        print(x,goal,count)

    return ans



print(numOfSubArrayWithSum( [0,0,0,0,0],0))