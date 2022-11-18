# divide and conquer algorithm
# first pick a pivot, then sort the array based on the pivot
# Time complexity: O(nlogn)
# Worst case: O(n^2)

def quickSort(array,low,high):   
    if low < high:        
        pivot = partition(array,low,high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)        

def partition(array, low, high):
    pivot = low
    index = low + 1 

    for i in range(index,high+1):
        if array[i] < array[pivot]:
            array[i], array[index] = array[index], array[i]
            index += 1 
    
    array[pivot], array[index-1] = array[index-1], array[pivot]
    return index - 1 

if __name__ == "__main__":
    array = [12,8,2,20,9,6]   
    quickSort(array,0,len(array)-1)
    print(array)

# refer: 
# https://www.runoob.com/w3cnote/quick-sort-2.html
