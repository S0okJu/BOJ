from itertools import combinations

# 입력 받기
l, c = map(int, input().split())
letters = sorted(input().split())  # 알파벳을 정렬된 상태로 입력받기

# 모음 정의
vowels = {'a', 'e', 'i', 'o', 'u'}

# 가능한 조합 생성 및 필터링
for combo in combinations(letters, l):
    # 모음 개수와 자음 개수 세기
    v_count = sum(1 for ch in combo if ch in vowels)
    cs_count = l - v_count  # 전체 길이에서 모음 개수를 뺀 것이 자음 개수

    # 조건에 맞는 경우 출력
    if v_count >= 1 and cs_count >= 2:
        print("".join(combo))  # 조합을 문자열로 변환하여 출력
