# divide and conquer algorithm
# first pick a pivot, then sort the array based on the pivot
# Time complexity: O(nlogn)
# Worst case: O(n^2)

def quickSort(array,low,high):   
    if low < high:        
        pivot = partition(array,low,high)
        quickSort(array, low, pivot)
        quickSort(array, pivot+1, high)        

def partition(array, low, high):
    pivot = low
    index = low + 1 

    # shift the numbers less than the pivot forward
    for i in range(index,high):
        if array[i] < array[pivot]:
            array[i], array[index] = array[index], array[i]
            index += 1 
    # print()
    # print("pivot:", array[pivot])
    # print("index:", array[index-1])

    # move the pivot to the correct position, where arr[pivot-i] are elements
    # less than pivot and arr[pivot+i] are elements greaer than pivot 
    array[pivot], array[index-1] = array[index-1], array[pivot]
    #return the index of the pivot
    return index - 1 

if __name__ == "__main__":
    array = [12,8,2,20,9,6]   
    array = [4,12,9,2,20,8,6,10,29,100,-2,-30,-25,-6,18,33,53,66] 
    quickSort(array,0,len(array))
    print(array)

# refer: 
# https://www.runoob.com/w3cnote/quick-sort-2.html
