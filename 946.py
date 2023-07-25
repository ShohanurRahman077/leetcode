from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popList = deque(popped)
        ans = []
        for x in pushed:
            ans.append(x)
            while popList and ans and ans[-1] == popList[0]:
                ans.pop()
                popList.popleft()
        return  len(ans) == 0
        