class Solution:
    def rotate(self, matrix):
        print(matrix)
        n = len(matrix)
        print(n//2)
        print((n+1)//2)
        for i in range(n//2):
            for j in range((n+1)//2):
                print(i, j)
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
                print(matrix)
    
    def run(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.rotate(matrix)
    
sol = Solution()
sol.run()
