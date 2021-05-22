class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
