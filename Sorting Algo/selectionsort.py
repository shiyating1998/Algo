# selection sort
# go through the array, select the smallest element, put the smallest element in its order
# go through the above process repeatedly 

# Time complexity: O(n^2), regardless of the input type, works ok with small input size 

def selectionSort(arr):
    n = len(arr)
    # n-1 since if n-1 are in its right place, then the rest will be at its correct position
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex!=i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]    
    return arr

if __name__ == "__main__":
    array = [12,8,2,20,9,6,-2,-5,6,9,100,234,34,-344]   
    print(selectionSort(array))
    #print(array)    