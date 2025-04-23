X = 'abcabcsaaaaaa'
Y = 'avcbbrdcdaaaaaaa'

C = []
B = []
for i in range(len(X)):
    C.append([])
    B.append([])
    for j in range(len(Y)):
        C[i].append(0)
        B[i].append('')

answer = ''

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            C[i][j] = C[i-1][j-1] + 1
            B[i][j] = 'A'

        elif C[i-1][j] > C[i][j-1]:
            C[i][j] = C[i-1][j]
            B[i][j] = 'U'
        else :
            C[i][j] = C[i][j-1]
            B[i][j] = 'L'

print(C[-1][-1])


