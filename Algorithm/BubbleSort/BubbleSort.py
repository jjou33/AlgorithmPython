'''
1. 정렬 (sorting) 이란?
정렬 (sorting): 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
정렬은 프로그램 작성시 빈번하게 필요로 함
다양한 알고리즘이 고안되었으며, 알고리즘 학습의 필수
다양한 정렬 알고리즘 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을 이해하고, 각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음

2. 버블 정렬 (bubble sort) 란?
두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

데이터 길이 / 조건체크 / 턴
2           1       1
3           2       2
4           3       3

'''
import random
def bubblesort(data):
    for i in range(len(data) - 1):
        swap = False # 한번도 변경이 없을 시 break
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True # 변경이 생기면 swap 값을 True로 변경
        if swap == False:
            break
    return data

if __name__ == '__main__':
    data = random.sample(range(100), 50)
    print(bubblesort(data))

