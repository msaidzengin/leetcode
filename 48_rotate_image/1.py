class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i, row in enumerate(zip(*matrix)):
	        matrix[i] = list(reversed(row))