# bubblesort O(n^2)
# from the beginning of the array, if arr[i] > arr[i+1], swap
# each run will guarantee to have the largest number to be at the end of the array
# thus needs n-1 rounds 
# each round needs to compare n-j times, where j is the number of rounds 
# for example, if j=2 then we need to compare n-2 times, since the last element is
# already in its place
# [12,8,2,20,9,6]  -----after the first round------> [8,2,12,9,6,20]
# 20 is already in its place

def bubbleSort(arr):
    n = len(arr)
    # n-1 rounds 
    for i in range(1,n):
        # n-i comparisons
        for j in range(0,n-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# Best case: when the array is sorted, no swapping operation, but still needs
# O(n^2) comparison operation
# Worst case: when the array is revserly sorted, needs to swap every node 


if __name__ == "__main__":
    array = [12,8,2,20,9,6]   
    bubbleSort(array)
    print(array)    


#refer: https://www.runoob.com/w3cnote/bubble-sort.html