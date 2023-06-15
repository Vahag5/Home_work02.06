hin_matric = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
sharq = 4 # @ndhanur depqum karanq  = len(hin_matric[0])
tox = 4   #                         =  len(hin_matric)    
nor_matric = [[0] * 4 for k in range(4)]
#Sarqecinq nor matric 4x4 copy ov phordzel em chi stacvum 

for i in range(tox):
    for j in range(sharq):
        nor_matric[i][j] = hin_matric[tox - i - 1][sharq - j - 1]
for tox in nor_matric:
    print(' '.join(str(arjeq) for arjeq in tox))

