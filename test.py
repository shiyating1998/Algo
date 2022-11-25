from heapq import heappush, heappop

pq = []
heappush(pq, (3,'A'))
heappush(pq, (3,'B'))
  
while pq:
    count = 0 
    while pq and count < 2:
        count += 1 
        a,b = heappop(pq)
        print(a,b)