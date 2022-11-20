# heapsort
# first build a max-heap tree based on the values in the array
# a max-heap is a complete tree where the parent is greater than its child 

# a heap is being built bottom up, by heapifying the second-last row, and up

# heapsort from a max-heap:
# pop out the top (swap top node with the last node) one by one
# and heapify from the top, since it is out of the order O(logn)


# Time complexity: O(nlog)

def heapify(tree, n, i):
    max = i
    c1 = 2*i+1
    c2 = 2*i+2
    if c1<n and tree[c1]>tree[max]:
        max = c1
    if c2<n and tree[c2]>tree[max]:
        max = c2
    
    if max!=i:
        if max==c1:
            tree[i],tree[c1] = tree[c1],tree[i]
            heapify(tree,n,c1)
        else:
            tree[i],tree[c2] = tree[c2],tree[i]
            heapify(tree,n,c2)    

def buildMaxHeap(tree,n):
    lastNode = n - 1 
    for j in range((lastNode-1)//2,-1,-1):
        heapify(tree,n,j)

def heapsort(tree, n):
    buildMaxHeap(tree,n)
    for i in range(n-1,0,-1):
        tree[0],tree[i] = tree[i],tree[0]
        heapify(tree, i, 0)
    return tree

tree1 = [0, 5, 20, 3, 8, 14, 6, 22]

tree2 = [0, 5, 5, 3, 8, 14, 6, 22, 14, 18]

tree3 = [-2, 5, 6, 8, 9, 12, 5, 3, 8, 14, 6, 22, 14, 18]

heapsort(tree1,len(tree1))

print(tree1)
# buildHeap(tree), heapify from bottom

# get from heap, swap, and heapify

# refer: https://www.runoob.com/w3cnote/heap-sort.html
# extremely clear: https://www.youtube.com/watch?v=j-DqQcNPGbE