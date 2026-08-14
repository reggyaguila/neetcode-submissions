class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int, left=0, right=None) -> bool:
        #Mid = left + right // 2
        #Left = 0
        #Right = m * n - 1
        if right == None:
            right = len(matrix) * len(matrix[0]) - 1

        if left > right:
            return False
    
        mid_flat_index = (right + left) // 2
        mid_row = mid_flat_index // len(matrix[0])
        mid_col = mid_flat_index % len(matrix[0])

        mid = (mid_row, mid_col)

        if target == matrix[mid[0]][mid[1]]:
            return True

        if target > matrix[mid[0]][mid[1]]:
            return self.searchMatrix(matrix, target, mid_flat_index + 1, right)
        
        if target < matrix[mid[0]][mid[1]]:
            return self.searchMatrix(matrix, target, left, mid_flat_index - 1)


        