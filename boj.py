N, K = map(int, input().split())

prime = [True for i in range(N+1)]
num = 1


for i in range(2, N+1):
    if prime[i]:
        j = i
        while j <= N:
            if prime[j] == False:
                num-=1
            if num == K:
                print(j)
            prime[j] = False
            j += i
            num += 1