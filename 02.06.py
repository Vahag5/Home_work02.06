hin_matrix = [
    ['0', 'M', '0', 'M', '0'],
    ['0', '0', 'M', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', 'M', 'M', '0', '0'],
    ['0', '0', '0', 'M', '0']
]

def matrix_M(matrix):
    sharq = len(matrix)  
    tox = len(matrix[0])  
    for i in range(sharq):
        for j in range(tox):
            if matrix[i][j] != 'M':
                count = 0
                for row in range(i - 1, i + 2):
                    for col in range(j - 1, j + 2):
                        if 0 <= row < sharq and 0 <= col < tox and matrix[row][col] == 'M':
                            count += 1
                matrix[i][j] = count

    return matrix

for tox in hin_matrix:
    print(tox)
nor_matrix = matrix_M(hin_matrix)
for tox in nor_matrix:
    print(tox)

