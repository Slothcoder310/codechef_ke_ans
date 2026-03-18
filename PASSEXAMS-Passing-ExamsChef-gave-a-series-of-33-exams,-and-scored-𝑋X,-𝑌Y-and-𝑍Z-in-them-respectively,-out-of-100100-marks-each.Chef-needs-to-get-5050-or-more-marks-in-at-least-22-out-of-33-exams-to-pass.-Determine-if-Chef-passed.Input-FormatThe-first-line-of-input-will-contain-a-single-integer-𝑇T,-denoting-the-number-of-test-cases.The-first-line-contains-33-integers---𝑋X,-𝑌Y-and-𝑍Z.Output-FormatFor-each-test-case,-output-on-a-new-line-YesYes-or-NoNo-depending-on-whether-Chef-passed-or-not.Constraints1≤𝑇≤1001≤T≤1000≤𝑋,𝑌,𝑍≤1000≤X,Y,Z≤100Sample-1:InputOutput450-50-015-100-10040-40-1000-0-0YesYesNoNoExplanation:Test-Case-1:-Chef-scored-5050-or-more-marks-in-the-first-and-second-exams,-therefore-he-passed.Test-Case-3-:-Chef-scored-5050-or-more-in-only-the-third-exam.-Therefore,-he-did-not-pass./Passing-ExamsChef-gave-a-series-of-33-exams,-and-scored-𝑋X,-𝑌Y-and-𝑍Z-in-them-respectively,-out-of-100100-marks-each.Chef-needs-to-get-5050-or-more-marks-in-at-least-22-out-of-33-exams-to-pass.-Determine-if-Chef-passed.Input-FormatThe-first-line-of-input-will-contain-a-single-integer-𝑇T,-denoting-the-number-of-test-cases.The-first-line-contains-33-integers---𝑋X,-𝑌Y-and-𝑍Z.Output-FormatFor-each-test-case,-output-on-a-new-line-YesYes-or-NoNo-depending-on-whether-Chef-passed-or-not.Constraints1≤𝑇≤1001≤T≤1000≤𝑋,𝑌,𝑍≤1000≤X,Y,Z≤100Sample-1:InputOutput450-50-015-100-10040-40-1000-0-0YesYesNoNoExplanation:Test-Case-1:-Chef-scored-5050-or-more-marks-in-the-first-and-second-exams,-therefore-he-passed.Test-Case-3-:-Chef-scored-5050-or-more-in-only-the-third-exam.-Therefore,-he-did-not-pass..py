# cook your dish here
test = int(input())
for _ in range(test):
    lst = list(map(int, input().split()))
    
    counter = 0
    
    for i in lst:
        if i >= 50:
            counter += 1
    
    if counter > 1:
        print("Yes")
    else:
        print("No")