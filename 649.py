class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_queue = deque()
        d_queue = deque()
        length = len(senate)
        for i,s in enumerate(senate):
            if s == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        print(r_queue,d_queue)

        while r_queue and d_queue:
            r_next = r_queue.popleft()
            d_next = d_queue.popleft()
            if r_next>d_next:
                d_queue.append(d_next +length)
            else:
                r_queue.append(r_next +length)
        print(r_queue,d_queue)
        return "Radiant" if r_queue else "Dire"
         
                