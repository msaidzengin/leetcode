class Solution:
    def rotate(self, matrix):

        for i, row in enumerate(zip(*matrix)):
	        matrix[i] = list(reversed(row))

        print(matrix)
            
    def run(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.rotate(matrix)
    
sol = Solution()
sol.run()
