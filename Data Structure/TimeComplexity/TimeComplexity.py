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

## 2n^2 + 3n 이라면 가장 높은 차원의 차수로 따른다 O(n^2)

class TimeComplexity:
    def sum_all(self, n):
        total = 0
        for num in range(1, n+1):
            total += num
        return total

    def sum_all2(self, n):
        return int(n * (n + 1) / 2)


if __name__ == '__main__':
    a = TimeComplexity()
    result = a.sum_all(100)
    print("-----", result)
    ##result = a.sum_all2(100)
    print("-----", result)

