# https://leetcode.com/problems/task-scheduler/description/
# Date: 11/25/2022

# https://leetcode.com/problems/task-scheduler/solutions/2847700/detailed-explanation-python-solution/

# Use a max heap to maintain the tasks, with the most freq first.
# Pop them out in rounds, where n+1 iterations are performed each round. Since for a same task to be performed again, it needs a total time 1 (perform the task) + n(wait).
# For example, ['A', 'A'], n = 2.
# 'A', idle, idle <---- 1 + n units of time
# for the next 'A' task to be performed

# Time complexity:
# O(n) for list itertaion and each task essentially goes through once.
# heappush and heappop O(logn)

# Space complexity:
# O(n) for the heap and the dic

from heapq import heappush, heappop
from collections import defaultdict
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # least number of units of times 
        # use the greedy approach
        # schedule the most frequent tasks first

        if n==0:
            return len(tasks)
      
        # count the freq of each task
        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1 
        
        # max heap to store the most freq tasks
        pq = []
        for key in dic:
            heappush(pq,(-dic[key],key))

        output = 0

        while pq:
            temp = [] # a temp to store the tasks scheduled this round 
            k = n + 1 # if n=2, then k=3, because after a task is performed, it needs to wait 
                      # for n times to be performed again, thus 1 + n is the total unit of time
                      # for it to be able to perform again
            while k > 0 and len(pq):
                count, task = heappop(pq)
                k -= 1 
                if -count > 1: # if there are more of this task to be performed, add to the temp
                               # since they can only be performed next round     
                    temp.append((count+1,task))            
                output += 1  # increment one unit of time 
            # when the round is completed, move all the next round 
            # tasks to pq 
            for node in temp:
               heappush(pq, node)
            # if the queue is not empty, append the idle time 
            if pq:
                output += k

        return output 


case1_tasks = ["A","A","A","B","B","B"]
case1_n = 2 
sol = Solution()
print("expected 8")
print("case 1: ", sol.leastInterval(case1_tasks,case1_n))

case2_tasks = ["A","A","A","B","B","B"]
case2_n = 0
sol = Solution()
print("expected 6")
print("case 2: ", sol.leastInterval(case2_tasks,case2_n))

case3_tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
case3_n = 2 
sol = Solution()
print("expected 16")
print("case 3: ", sol.leastInterval(case3_tasks,case3_n))