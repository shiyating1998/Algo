# countingSort, not a comparison sort, it is more like a linear sort
# condition: only works with numbers, and there is a certain range of numbers
# for example, numbers from 0-99

# Steps:
# separte them into buckets O(n)
# combine them into arrays O(n)

# Space Complexity: O(n) for the buckets

def countingSort(arr):
    buckets = [0] * (max(arr)+1 - min(arr))       
    for val in arr:
        buckets[val] += 1 
    
    index = 0
    for i in range(min(arr),max(arr)+1):
        while buckets[i]>0:
            buckets[i] -= 1 
            arr[index] = i
            index += 1 
    return arr  


# refer: https://www.runoob.com/w3cnote/counting-sort.html
def countingSort2(arr):
    bucketLen = max(arr)+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):       
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr

arr = [0,2,2,2,9,9,9,4,4,4,4,4,4,4,100,99,88,33,44,-8,23,245,-4,-34]
print(countingSort(arr))
print(countingSort2(arr))