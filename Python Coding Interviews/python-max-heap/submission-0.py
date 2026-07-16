import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    for i in nums:
        
        heapq.heappush(heap, -i)
    
    reversed_nums = []
    while len(heap) != 0:
        reversed_nums.append(-heapq.heappop(heap))

    return reversed_nums



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
