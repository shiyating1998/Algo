# mergesort
# Time complexity: O(nlogn) independent of the original array
# divide and conquer algorithm
# divide the array into halves, sort the first half, sort the second half, combine them

def mergesort(arr):
    if len(arr)>1:
        mid = (len(arr))//2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        arr = merge(left,right)
        #print("arr:",arr)        
    return arr 

def merge(left,right):
    arr = [0]*(len(left)+len(right))

    i = 0
    j = 0
    k = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k] = left[i]
            i += 1 
        else:
            arr[k] = right[j]
            j += 1 
        k += 1 
    
    while i!=len(left):
        arr[k] = left[i]
        k += 1 
        i += 1 
    while j!=len(right):
        arr[k] = right[j]
        k += 1 
        j += 1 

    return arr

arr = [0,2,2,2,9,9,9,4,4,4,4,4,4,4,100,99,88,33,44,-8,23,245,-4,-34]
print(mergesort(arr))
tree3 = [-2, 5, 6, 8, 9, 12, 5, 3, 8, 14, 6, 22, 14, 18]
print(mergesort(tree3))

# refer: https://www.runoob.com/w3cnote/merge-sort.html