class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row*col - 1
        while l <= r :
            mid = (l + r) // 2

            rows = mid // col
            cols = mid % col
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
