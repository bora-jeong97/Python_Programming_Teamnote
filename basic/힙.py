'''
기본적으로 최소 힙(Min Heap)으로 구성되어 있어 힙에 원소를 넣었다가 빼면 오름차순 정렬이 된다
최소 힙 자료구조의 최상단 원소는 항상 '가장 작은 원소'이기 때문이다

- 시간 복잡도 : O(NlogN)
- heapq.heappush() : 힙에 원소 삽입하기
- heapq.heappop() : 힙에 원소 꺼내기

'''

import heapq


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 6, 2, 0, 4, 7, 5])
print("오름차순 힙 정렬 : ", result)


import heapq


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 6, 2, 0, 4, 7, 5])
print("내림차순 힙 정렬 : ", result)