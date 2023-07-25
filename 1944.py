def canSeePersonsCount( heights: list[int]) -> list[int]:
        
        n = len(heights)
        ans = [0]*n
        inc_stack = []
        for i in range(n-1, -1, -1):
            total = 0
            while inc_stack and heights[i]> inc_stack[-1]:
                inc_stack.pop()
                total+=1
            if inc_stack:
                total+=1
            inc_stack.append(heights[i])
            ans[i] = total
            
        
        return ans


print(canSeePersonsCount([5,1,2,3,10]))