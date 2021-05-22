class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        half = (math.ceil(len(matrix) / 2))
        
        r = None
        if len(matrix) % 2 == 0:
            r = range(half)
        else:
            r = range(half - 1)

        for y in r:
            for x in range(half):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[-1 - x][y]
                matrix[-1 - x][y] = matrix[-1 - y][-1 - x]
                matrix[-1 - y][-1 - x] = matrix[x][-1 - y]
                matrix[x][-1 -y] = tmp
