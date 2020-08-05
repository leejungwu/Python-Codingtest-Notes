N, K = map(int, input().split())

prime = [True for _ in range(N + 1)]
num = 1

for i in range(2, N+1):
    if prime[i] == True:
        for j in range(i, N + 1, i):
            if prime[j] == False:
                continue
            if num == K:
                print(j)
            prime[j] = False
            num += 1