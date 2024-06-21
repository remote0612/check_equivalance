# -*- coding: utf-8 -*-
"""equiv_relation_check_student.ipynb의 사본

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wHbz4F-Qhudpv0FJ4wpCMx_uo8im9lGh

# 관계 R 이 set 으로 주어질 때, 이 관계 R 이 동치 관계인지를 판단하는 파이썬 모듈을 만들라. 이 모듈에는 check_transitive(R), check_symmetric(R), check_reflexive(R) 을 포함하며, 이 함수들은 True, False 를 반환한다. 이 결과를 종합하여, 동치관계인지 판단하는 check_equivalance(R) 도 들어있는데, 이 함수에서 위의 세 함수 (즉, check_transitive(R), check_symmetric(R), check_reflexive(R)) 을 호출하여 해당 결과들을 종합하여 동치 관계 여부를 판단하고, True 혹은 False 를 최종적으로 반환해준다. 이 모듈이 팀원들의 깃페이지에 read.md 와 함께 기록되어 다운 받으면 설치 후 각 함수를 실행될 수 있도록 한다.

## 결과는 모든 집합 형태의 관계에 대해 작동해야하지만, 특히 아래의 예로 주어지는 집합에 대해 작동하도록 한다.

```
A = {1,2,3,4} # 관계가 정의된 집합
R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)} # 정의된 관계
```
"""

def check_transitive(R):
  lis=[]
  s=0
  for i in R:
    if s==0:
      x=i[0]
      y1=i[1]
      s=1
      continue
    y2=i[0]
    z=i[1]
    if y1==y2:
      if (x,z) in R:
        lis.append(True)
      else:
        lis.append(False)
    x=y2
    y1=z
  return all(lis)
