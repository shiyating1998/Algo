# insertion sort 
# from the second element, compare to the elements before it, and insert it to the right place
# the elements before the currently selected element are sorted 
# Time Complexity O(n^2)

# 实操跟理解是天差地别的！
# 不要只是看代码，要跟着码出来

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        pre = i - 1
        # from back to front, compare to the element to be inserted
        # if it is bigger, then shift back
        while pre >= 0 and arr[pre] > current:
            arr[pre + 1] = arr[pre]
            pre -= 1 
        # if the arr[pre] is smaller than the element to be inserted
        # then arr[pre+1] is the correct position for the inserted element 
        arr[pre + 1] = current 
    return arr

if __name__ == "__main__":
    array = [2,6,9,12,18,10]   
   # array = [9,23,4,-23,23,-33,4,0,3,4,5,2,-4]
    array = [0,9,-2,3,4,5,10,18,10]
    print(insertionSort(array))
    