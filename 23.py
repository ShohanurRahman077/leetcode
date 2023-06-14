arr = [1, 0]
arr_length = len(arr)
print (arr_length)
for i in range(arr_length):
    for x in range(i+1,arr_length):
        if arr[i]> arr[x]:
            temp = arr[i]
            arr[i] = arr[x]
            arr[x] = temp

print (arr)
    
