def partition(low,high,arr):
    print ('step --->'+str(low))
    i,j = low,high
    pivot = arr[low]
    print ( low,high,pivot)
    i,j = low,high
    while i<j:
        while arr[i]<=pivot:
            i=i+1
        while arr[j]>=pivot:
            j=j-1    
        print (i,j)





arr = [ 4, 1, 3, 9, 7]
low,high = 0, len(arr)
if (low <high ):
    j = partition(low,high,arr);

