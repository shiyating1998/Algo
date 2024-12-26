# https://leetcode.cn/problems/design-linked-list/description/
# 707. Design Linked List

# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 

# Constraints:

# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

class MyNode:
    def __init__(self, val=-1):
        self.next = None
        self.val = val 

class MyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.count = 0

    def get(self, index: int) -> int:
        if (index >= self.count):
            return -1
        
        cur = self.head 
        while index > 0:
            cur = cur.next 
            index -= 1 
        return cur.val 

    def addAtHead(self, val: int) -> None:
        newNode = MyNode(val)
        if self.count == 0: 
            self.head = newNode 
            self.tail = newNode 
        else:
            newNode.next = self.head 
            self.head = newNode
        self.count += 1  


    def addAtTail(self, val: int) -> None:
        newNode = MyNode(val)
        if self.count == 0:
            self.tail = newNode 
            self.head = newNode 
        else: 
            self.tail.next = newNode
        
            self.tail = newNode
        self.count += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count or index < 0:
            return 
        if index == 0:
            self.addAtHead(val)
        elif index == self.count:
            self.addAtTail(val)
        else:
            prev = self.head 
            while index > 1:
                prev = prev.next 
                index -= 1 
            after = prev.next 
            newNode = MyNode(val)
            prev.next = newNode 
            newNode.next = after 
            self.count += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return 

        if self.count == 1 and index == 0:
            self.head = None 
            self.tail = None 
            self.count = 0 

        if index < self.count: 
            self.count -= 1 
            t , h = False, False
            if index == self.count:
                t = True 
            if index == 0:
                h = True 
            dummy = MyNode()
            dummy.next = self.head 

            cur = dummy 
            while index > 0:
                cur = cur.next 
                index -= 1 
            cur.next = cur.next.next 
            if t: 
                self.tail = cur 
            if h:
                self.head = dummy.next 
 



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Note: 今天设计的是单链表，不过实现中记录了尾节点，并要在每个操作中更新尾节点的信息。经常这里出错那里出错……下次是不是不玩儿花活了。或者起码把基础的先做好