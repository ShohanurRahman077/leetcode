from collections import defaultdict
def equalPairs(grid: list[list[int]]):
    column = []
    ans = 0
    for i in range(len(grid)):
        temp = grid[i]
        columnTemp = [] 
        for j in range(len(temp)):
            columnTemp.append(grid[j][i])
        column.append(columnTemp)

    for x in grid:
        for y in column:
            if x ==y:
                ans+=1

    return (ans)
            
def equalPairsWithHashMap(grid: list[list[int]]) -> int:
        def convert_to_key(arr):
            # Python is quite a nice language for coding interviews!
            return tuple(arr)
        
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            
            dic2[convert_to_key(current_col)] += 1
        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        print(ans)
        return ans


equalPairsWithHashMap([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])