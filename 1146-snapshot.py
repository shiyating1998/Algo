# https://leetcode.com/problems/snapshot-array/description/

class SnapshotArray:
    # O(n) for initialization of array
    def __init__(self, length: int):
        # arr[i] ---> a list of [snap_id, val]
        self.arr = [[[-1,0]] for _ in range(length)]
        self.snap_id = 0 

    # O(1)
    def set(self, index: int, val: int) -> None:
        #print(self.arr[index][-1][1])
        self.arr[index].append([self.snap_id, val])

    # O(1)
    def snap(self) -> int:
        self.snap_id += 1 
        return self.snap_id - 1 
        
    # O(logn) binary search, for the rightmost snap_id
    def get(self, index: int, snap_id: int) -> int:
        table = self.arr[index]
        low = 0
        high = len(table) - 1 
        while low <= high:
            mid = (low+high)//2
            if table[mid][0]==snap_id:
                low = mid + 1 
            elif table[mid][0]>snap_id:
                high = mid - 1 
            else:
                low = mid + 1 

        return table[low-1][1]        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

sp = SnapshotArray(3)
sp.set(0,5)
sp.snap()
sp.set(0,6)
print(sp.get(0,0))

# ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]