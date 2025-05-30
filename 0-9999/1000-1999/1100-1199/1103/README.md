# 게임

- 골드 2
- https://www.acmicpc.net/problem/1103

## 문제 조건

- 작동 조건

  1. 동전이 있는 곳에 쓰여 있는 숫자 X를 본다.
  2. 위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다.
  3. 동전을 위에서 고른 방향으로 X만큼 움직인다. 이때, 중간에 있는 구멍은 무시한다.

- 게임 종료 조건

  - 구멍에 도착
  - 보드의 바깥에 나간다.

- 무한번 움직일 수 있음

### 입력값

- NxM 크기의 표

### 출력값

- 동전을 움직일 수 있는 최대값
- 동전을 무한대로 움직일 수 있는 경우 -1 출력

## 풀이

- 동전을 무한번 움직일 수 있다는 점에서 BFS 재귀 방식을 활용함

### 의사코드

```text
N,M, graph(N*M)를 입력받음

Function solution
    결과값을 저장할 dp 변수, 방문 여부 리스트, 무한 루프 변수

    Function DFS(x,y)
        if 그래프 범위에 벗어난다면
            return 0
        endif

        if x,y 위치에 구멍이 있다면
            return 0
        endif

        if x,y가 이미 방문되었다면
            무한 루프 여부 체크
            return 0
        endif

        if dp(결과값)에 답이 존재한다면
            return x,y의 dp 값 반환
        endif

        x,y 방문 표시
        최대 이동값 설정
        for 상하좌우
            이동할 위치 mx,my 설정
            if 이동할 위치가 방문되지 않았다면
                이동할 위치 방문 수행 체크
                DFS(이동할 위치 x, y)
                최대 이동값 += 1
            endif

        x,y에서 가장 많이 방문한 횟수를 dp에 저장함
        x,y 방문 표시 취소

    DFS(0,0)를 통해 최대 이동 횟수의 값을 구함

    if 무한루프가 존재
        -1 출력
    else
        결과값 출력
    endif
```

### 시간 복잡도

```math
O(N \time M)
```

### 소스코드

- [Python](./1103.py)

### 기타

#### Python

- 무한이 움직일 수 있다는 조건이 존재할 경우 Stack를 활용한 DFS 구현을 생각하자
- 파이썬의 경우 기본 재귀 횟수가 1000번으로 제한되어 있다. 그러므로 `sys.setrecursionlimit(10000)` 를 통해 재귀 횟수를 늘리자.
