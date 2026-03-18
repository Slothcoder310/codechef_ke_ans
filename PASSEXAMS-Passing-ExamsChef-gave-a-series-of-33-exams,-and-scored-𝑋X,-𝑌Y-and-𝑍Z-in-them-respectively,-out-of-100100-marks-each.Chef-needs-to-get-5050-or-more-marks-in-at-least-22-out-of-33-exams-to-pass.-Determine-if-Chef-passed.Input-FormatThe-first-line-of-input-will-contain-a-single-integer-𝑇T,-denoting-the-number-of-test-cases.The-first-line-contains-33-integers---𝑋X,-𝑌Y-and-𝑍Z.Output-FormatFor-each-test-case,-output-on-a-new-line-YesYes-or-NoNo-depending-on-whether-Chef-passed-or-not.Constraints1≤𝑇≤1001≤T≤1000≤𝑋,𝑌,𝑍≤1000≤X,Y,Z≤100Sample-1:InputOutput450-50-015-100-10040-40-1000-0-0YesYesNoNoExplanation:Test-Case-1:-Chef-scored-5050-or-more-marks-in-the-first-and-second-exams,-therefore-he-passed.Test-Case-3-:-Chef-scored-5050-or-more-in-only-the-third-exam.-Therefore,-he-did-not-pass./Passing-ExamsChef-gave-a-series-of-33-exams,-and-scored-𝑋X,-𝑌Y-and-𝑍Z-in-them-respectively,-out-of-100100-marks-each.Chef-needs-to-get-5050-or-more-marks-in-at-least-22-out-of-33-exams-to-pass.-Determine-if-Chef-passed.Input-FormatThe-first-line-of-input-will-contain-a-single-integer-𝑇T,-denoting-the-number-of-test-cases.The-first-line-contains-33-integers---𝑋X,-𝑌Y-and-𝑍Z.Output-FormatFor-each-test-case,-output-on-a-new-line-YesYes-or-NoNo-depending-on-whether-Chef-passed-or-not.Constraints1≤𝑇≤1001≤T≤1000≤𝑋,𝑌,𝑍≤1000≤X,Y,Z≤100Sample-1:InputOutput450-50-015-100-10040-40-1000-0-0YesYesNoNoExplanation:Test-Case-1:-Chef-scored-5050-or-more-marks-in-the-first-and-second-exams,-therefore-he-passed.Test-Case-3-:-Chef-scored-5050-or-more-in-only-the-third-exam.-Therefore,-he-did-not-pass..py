# cook your dish here
test = int(input())
for _ in range(test):
    first, second, third = map(int, input().split())
    
    if first >= 50 and second >= 50:
        print("Yes")
    elif first >= 50 and third >=0:
        print("Yes")
    elif second >= 50 and third >= 50:
        print("Yes")
    else:
        print("No")
        