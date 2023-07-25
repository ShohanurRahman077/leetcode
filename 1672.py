def maximumWealth(accounts: list[list[int]]):
    maxWealth = 0
    for x in accounts:
        sum = 0
        for y in x:
            sum+=y
        maxWealth = max(sum,maxWealth)
    return maxWealth



maximumWealth([[1,5],[7,3],[3,5]])