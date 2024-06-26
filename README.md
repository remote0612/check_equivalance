# **check_equivalance**
### *코드 설명-pkg 폴더 안의 코드*
#### 1.check_reflexive (반사적 관계인지 확인하는 코드)
* 집합 A 안의 원소를 하나씩 불러온다.
* 해당 원소 a에 대해 (a, a)∈R가 존재한다면 s에 1 더하기, 아니라면 아무것도 해주지 않고 다음 원소에 대해 이 과정을 실행한다.
* 이 때, s의 초기값은 0이다.
* 이를 집합 안의 원소에 대해 전부 확인할 때까지 반복한다.
* s에 해당된 숫자가 집합에 존재하는 원소의 개수와 같다면 True를 반환, 아니라면 False를 반환을 한다.


#### 2. check_symmetric (대칭적 관계인지 확인하는 코드)
* li라는 빈 리스트를 지정해준다.
* 관계 R에 존재하는 순서쌍을 하나씩 불러온다.
* 순서쌍의 정의역을 변수 x, 치역을 변수 y로 지정해준다.
* 만약 정의역과 치역의 자리가 바뀐 (y,x)∈R이 존재한다면 li에 Ture를 더해주고, 존재하지 않는다면 Fasle를 더해준다.
* 이를 관계 안의 순서쌍에 대해 전부 확인할 때까지 반복한다.
* li 안에 Ture라는 값만 들어있으면 True를 반환, 아니라면 False를 반환을 한다.


#### 3. check_transitive (추이적 관계인지 확인하는 코드)
* li라는 빈 리스트를 지정해준다.
* 관계 R에 존재하는 순서쌍을 하나 불러온다.
* 첫 번째로 불러온 순서쌍의 정의역을 변수 x, 치역을 변수 y1로 지정해준다. 이후 continue를 사용해 다음 순서쌍을 불러와준다.
* 두 번째 순서쌍의 정의역을 변수 y2, 치역을 변수 z로 지정해준다.
* 조건문으로 y1과 y2가 같은지 확인해준다.
* 만약 위의 조건이 충족된 경우 (x,z)∈R가 존재하는지 확인한다.
* 존재한다면 li에 Ture를 더해주고, 존재하지 않는다면 Fasle를 더해준다.
* 다음 순서쌍을 확인하기 위해 y2=x로, z=y1으로 지정해준다.
* 이를 관계 안의 순서쌍에 대해 전부 확인할 때까지 반복한다.
* li 안에 Ture라는 값만 들어있으면 True를 반환, 아니라면 False를 반환을 한다.

### *코드 설명-pkg 폴더 밖의 코드*
#### 4. main (동치인지 확인하는 코드)
* 위의 세 코드의 값을 하나씩 저장한다.
* 값이 모두 Ture인 경우 Ture 반환, 아니라면 Fasle를 반환한다.
