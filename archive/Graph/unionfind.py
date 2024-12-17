
# union find
# to find the number of connected components in a graph
# reprensented by using an array: parent, where parent[x] is the parent of node x 
# reflexive property: p & p are connected
# symmetric property: if p & q are connected, then q & p are connected
# transitive property: if p & q are connected and q & r are connected, then p & r are connected 


class UnionFind:

    def __init__(self, n):
        self.count = n         # number of connected components 
        self.parent = [0] * n  # parent[x] is the parent node of x 
        for i in range(n):
            self.parent[i] = i
    

    # Important!!! The time complexity of the UNIONFIND algorithm depends on this!
    # since both connected and union depend on find()
    # some very delicate method of flatten the graph, can check article[1] to 
    # learn more 

    # find the root of x recursively
    # while flattening the graph 
    # averages out to be O(1)
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # union two nodes, connect them by joining them with the same root
    # O(1)
    def union(self,p,q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp!=rootq:
            self.parent[rootp] = rootq
            self.count -= 1
    
    # check if two nodes are connected by checking if they have the same root
    # O(1) since the graph is flat 
    def connected(self,p,q):
        return self.find(p)==self.find(q)

    

uf = UnionFind(10)
uf.union(1,2)
print(uf.count)
uf.union(1,3)
print(uf.connected(2,3))
print(uf.count)
uf.union(5,6)
print(uf.count)

# refer: 
# [1] https://labuladong.github.io/algo/2/22/53/

# Practice Problems：
# 1. https://leetcode.com/problems/surrounded-regions/
# 2. https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ (leetcode premium)
# 3. https://leetcode.com/problems/satisfiability-of-equality-equations/ 