lsh = [
    [0,0, 'M',0, 0],
    ['M',0, 0, 'M', 0],
    [0, 'M', 0, 0, 'M'],
    [0, 0, 0, 'M', 0],
    ['M', 0, 0, 0, 'M']
]

lsn = []
for i in range(5):
    stn = []
    for j in range(5):
        if lsh[i][j] == 'M':
            stn.append('M')
        else:
            tiv = 0
            for x in range(max(0, i - 1), min(i + 2, 5)):
                for y in range(max(0, j - 1), min(j + 2, 5)):
                    if lsh[x][y] == 'M':
                        tiv = tiv + 1
            stn.append(str(tiv))
    lsn.append(stn)
for row in lsn:
    print(' '.join(row))
