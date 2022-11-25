from heapq import heappush, heappop

def test(tasks,n):
     
    dic = defaultdict(int)

    for task in tasks:
        dic[task] += 1 
        
    pq = []
    for key in dic:
        #print(key)
        #print(dic[key])
        heappush(pq,(dic[key],key))
       # print(pq)

    output = 0

    while pq:
        count = 0 
        while pq and count <= n:
            count += 1 
            a,b = heappop(pq)
            print(a,b)
        # while pq:
        #     count = 0
        #     while count<n:
        #         count += 1 
        #         a,b = heappop(pq)
        #         print(a,b)
        # while pq:
        #     temp = []

        #     count = 0
        #     while count<n and len(pq)>0:
        #         c, task = heappop(pq)
        #         count += 1 
        #         if c > 1:                 
        #             temp.append((c,task))

        #     output += count 
            
           # for node in temp:
            #    heappush(pq, node)

    return output 

tasks = ["A","A","A","B","B","B"]
n = 2
test(tasks,n)