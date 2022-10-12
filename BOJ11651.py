testCase = int(input())

z = [[0] * 2 for j in range(testCase)]

for i in range(testCase):
    s = input()
    S = s.split(' ')
    
    z[i][0] = int(S[0])
    z[i][1] = int(S[1])
        
z.sort(key=lambda x:(x[0], x[1]))

for j in range(testCase):
    print(z[j][0], z[j][1])