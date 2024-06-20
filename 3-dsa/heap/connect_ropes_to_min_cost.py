# always take 2 min ropes 

import heapq


def connect_ropes(arr):
    heapq.heapify(arr)

    new_rope_cost = 0
    while(len(arr) > 1):
        first_rope = heapq.heappop(arr)
        second_rope = heapq.heappop(arr)

        new_rope_cost  += first_rope + second_rope
        heapq.heappush(arr, first_rope + second_rope)
    
    return new_rope_cost

print(connect_ropes([4, 3, 2, 6]))