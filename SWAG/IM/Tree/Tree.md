# Tree
## 1. 트리의 개념

> 한 개 이상의 노드로 이루어진 자료구조.  
> 각각 `node` 와 `edge` 로 이루어진다.  

- 루트 노드: 최상위 노드
- 형제 노드: 같은 부모를 둔 자식들의 노드
- 조상 노드: 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리: 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리(부분집합트리)
- 자손 노드: 서브트리에 있는 하위 레벨의 노드들.

### 1-1. 트리의 구성 요소
- 차수(degree): 노드에 연결된 자식 노드의 수
- 트리의 차수: 트리에 있는 노드의 차수 중 가장 큰 값.
- 단말 노드(leap node) 가장 최하단에 있는 노드. / 즉 차수가 0인 노드들
- 높이: 노드 중 최상위 노드(노드의 레벨)
    - 트리의 노드 중 높이가 가장 큰 값. (최대 레벨)


## 2. 이진 트리(Binary Tree)
> 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리  
> 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리  

### 1) 포화 이진 트리(Full binary Tree)
> 모든 레벨에 노드가 포화상태로 차 있는 이진 트리.  
> 항상 (2^h+1 -1)개의 노드를 갖는다. (가득 차있기 때문)  

### 2) 완전 이진 트리(Complete binary Tree)
> 높이가 h이고 노드 수가n개일 때, Full 이진 트리의 노드 번호가 1부터 n번까지 빈 자리가 없는 이진 트리.

### 3) 편향 이진 트리(Skewed binary Tree)
> 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리.

### `순회`(Traversal)
> 트리의 각 노드를 중복되지 않게 전부 방문하는 것을 말하는데,  
> 트리는 비선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
- 1. 전위 순회 (V - L - R)  
    - 자손노드부터 루트노드를 먼저 방문
        - 1) 현재 노드 n을 방문하여 처리 : V
        - 2) 현재 노드 n의 왼쪽 서브트리로 이동: L
        - 3) 현재 노드 n의 오른쪽 서브트리로 이동: R
- 2. 중위 순회 (L - V - R)
    - 왼쪽 자손, 루트, 오른쪽 자손 순
        - 1) 현재 노드 n의 왼쪽 서브트리로 이동: L
        - 2) 현재 노드 n을 방문하여 처리 : V
        - 3) 현재 노드 n의 오른쪽 서브트리로 이동: R
- 3. 후위 선회 (L - R - V)
    - 루트노드보다 자손을 먼저 방문
        - 1) 현재 노드 n의 왼쪽 서브트리로 이동: L
        - 2) 현재 노드 n의 오른쪽 서브트리로 이동: R
        - 3) 현재 노드 n을 방문하여 처리 : V

## 3. List를 이용한 Binary Tree의 표현(Expression Tree)
- 1. 이진 트리에 각 노드 번호를 부여.
- 2. 루트의 번호를 1로 함.
- 3. 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2n부터 2n+1 -1 까지 번호를 차례대로 부여

> 하지만 리스트를 사용하게 되면 불필요한 메모리 공간의 소비가 많아지게 되고,  
> 이러한 이유 때문에 쌍방향 링크드리스트를 이용하면 효율적으로 구현할 수 있게 된다.

## 4. 이진 탐색 트리(Binary search Tree)
> 탐색작업을 효율적으로 하기 위한 자료구조로, 여기저기 굉장히 많이 쓰임.
- 모든 원소는 서로 다른 유일한 키를 가짐
- Key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 왼쪽 서버트리와 오른쪽 서브트리도 이진 탐색 트리임
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있음.

### 1) 탐색 연산.
- 1. 루트에서 시작
- 2. 탐색할 키값 x를 루트 노드의 키값과 비교.
    - if 키값 x == 루트 key: 탐색 성공
    - elif x < 루트 노드: 왼쪽 서브트리 탐색
    - elif x > 루트 노드: 오른쪽 서브트리 탐색
- 3. 평균적으로 O(log n)의 시간복잡도를 갖지만, 한쪽으로 치우친 경우 O(n)의 탐색시간

### 2) 삽입 연산
- 1. 먼저 탐색 연산을 수행
    - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없다.
    - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다.

## 5. Heap
> 완전 이진 트리에 있는 노드 중 키값이 가장 큰 노드 or 가장 작은 노드를 찾기 위해 만든 자료구조 
- Max heap
- Min heap
- 중복된 키가 존재하는 경우 힙이 아닌 이진탐색드리이다.

**힙에서는 삽입과 삭제가 가장 중요**
### 1) 삽입 연산
- 1. 다음으로 빈 공간에 임의의 수를 넣음.
- 2. 부모노드와 크기를 비교하여 더 클 경우 자리를 바꿈.
- 3. 더이상 비교가 불가능할 때 멈춤(변화가 없을 때)

### 2) 삭제 연산
> 루트 노드의 원소만을 삭제할 수 있고, 힙의 종류에 따라 최대값 혹은 최소값을 구할 수 있다.
- 1. 루트 노드의 원소 삭제
- 2. 마지막 노드를 루트 노드 위치로 바꿈
- 3. 자식 노드가 부모노드보다 클 경우 자리를 바꿔줌.
**자리 확정**