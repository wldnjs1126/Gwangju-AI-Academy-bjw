import numpy as np
arr = np.random.randint(10,size=(3,4,5),dtype='int8')
print(arr)
# [[[1 5 3 8 7]
#   [7 9 5 2 3]
#   [3 5 1 7 2]
#   [1 0 4 0 0]]

#  [[6 4 1 1 2]
#   [0 2 6 9 7]
#   [3 7 9 4 6]
#   [4 4 1 6 5]]

#  [[1 5 9 0 3]
#   [0 3 0 1 6]
#   [0 3 8 1 7]
#   [7 4 0 9 4]]] -> (3,4,5) 크기의 배열이 생성됨, 0부터 9까지의 정수 중에서 랜덤하게 선택된 값으로 채워짐, 
#                    dtype='int8'로 지정했기 때문에 모든 원소가 8비트 정수형으로 생성됨

print(arr.ndim) # 차원 확인  (3세트, 4행, 5열 3차원)
print(arr.shape) # 크기 확인
print(arr.size) # 요소의 갯수 확인 (3*4*5 = 60)
print(arr.dtype) # 데이터 타입 확인
# 3
# (3, 4, 5)
# 60
# int8

lst = [1, 2, 3, 4, 5]

result = []

for i in lst:
    result.append(i * 10)

print(result)

arr = np.array(lst) # 브로드캐스팅 넘파이를 쓰는 이유중 하나
print(arr * 10)