test = int(input())

for _ in range(test):
    N, x = map(int, input().split())
    
    subscription = (N + 5) // 6
    
    print(subscription * x)