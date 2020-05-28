## O(1) 실행 횟수가 2회 일경우

n = 10
if n > 10:
    print(n)

## O(n) n에 따라, n번, n+10 번, 또는 3n+10 번등 실행한다

for num in range(3):
    for i in range(n):
        print(i)

## O(n^2) n, n^2, 100n^-100 ... etc

for i in range(300):
    for num in range(n):
        for index in range(n):
            print(index)


