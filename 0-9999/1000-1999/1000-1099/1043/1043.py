from typing import List
from collections import deque
import sys 
input = sys.stdin.readline

def solution(N:int, M:int, truth_people:List[int], parties:List[List[int]]) -> int:
    if not truth_people:
        return M

    q = deque(truth_people)
    visited_person = set(truth_people)
    visited_party = [False] * M

    while q:
        curr = q.popleft()
        for i in range(M):
            if visited_party[i]:
                continue
            if curr in parties[i]:
                for person in parties[i]:
                    if person not in visited_person:
                        visited_person.add(person)
                        q.append(person)
                visited_party[i] = True

    # 진실 퍼지지 않은 파티 개수
    count = 0
    for i in range(M):
        if not any(person in visited_person for person in parties[i]):
            count += 1

    return count
    
if __name__ == '__main__':
    N, M = map(int,input().split())
    
    truth = list(map(int,input().split()))
    if truth[0] > 0:
        truth_people = truth[1:]
    else:
        truth_people = []

    parties = []
    for _ in range(M):
        party = list(map(int,input().split()))    
        parties.append(party[1:]) 

    print(solution(N, M, truth_people, parties))
