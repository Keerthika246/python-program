def is_magic_square(matrix):
    n = len(matrix)
    
    sum_first_row = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != sum_first_row:
            return False
            
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != sum_first_row:
            return False
            
    if sum(matrix[i][i] for i in range(n)) != sum_first_row:
        return False
    if sum(matrix[i][n - i - 1] for i in range(n)) != sum_first_row: 
        return False
    
    return True    

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

if is_magic_square(matrix):
    print("Magic matrix")
else:
    print("Not a Magic Matrix")
