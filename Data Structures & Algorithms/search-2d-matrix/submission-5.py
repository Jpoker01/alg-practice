from itertools import chain

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_list = list(chain.from_iterable(matrix))
        left = 0
        right = len(matrix_list) - 1
        while left <= right:
            
            middle = (left + right) // 2

            if target > matrix_list[middle]:
                left = middle + 1
            elif target < matrix_list[middle]:
                right = middle - 1
            else:
                return True
        return False        