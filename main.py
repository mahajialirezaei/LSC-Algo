X = 'abcabcsaaaaaa'
Y = 'avcbbrdcdaaaaaaa'

C = []
B = []
for i in range(len(X) + 1):
    C.append([])
    B.append([])
    for j in range(len(Y) + 1):
        C[i].append(0)
        B[i].append('')

answer = ''

for i in range(1, len(X) + 1):
    for j in range(1, len(Y) + 1):
        if X[i - 1] == Y[j - 1]:
            C[i][j] = C[i-1][j-1] + 1
            B[i][j] = 'A'

        elif C[i-1][j] > C[i][j-1]:
            C[i][j] = C[i-1][j]
            B[i][j] = 'U'

        else :
            C[i][j] = C[i][j-1]
            B[i][j] = 'L'

print(C[-1][-1])

i = len(X)
j = len(Y)

while i > 0 and j > 0:
    print(i , j)
    if B[i][j] == 'A':
        answer += X[i-1]
        i -= 1
        j -= 1
    elif B[i][j] == 'U':
        i -= 1
    else:
        j -= 1

answer = reversed(answer)
print(''.join(answer))
