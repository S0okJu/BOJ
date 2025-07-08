from collections import defaultdict, Counter
import sys
input = sys.stdin.readline

def timeout():
    # 사전 입력 받기
    words = []
    while True:
        word = input().strip()
        if word == '-':
            break
        words.append(word)
    
    # 각 퍼즐판 처리
    while True:
        puzzle = input().strip()
        if puzzle == '#':
            break
        
        puzzle_counter = Counter(puzzle)
        puzzle_chars = set(puzzle)
        
        # 각 문자를 가운데에 놓았을 때의 단어 개수 계산
        result_count = defaultdict(int)
        
        for central_char in puzzle_chars:
            count = 0
            
            # 각 단어가 만들어질 수 있는지 확인
            for word in words:
                word_counter = Counter(word)
                
                # 1. 가운데 문자가 단어에 포함되어야 함
                if central_char not in word_counter:
                    continue
                
                # 2. 단어의 모든 문자가 퍼즐에 있어야 함
                if not all(char in puzzle_chars for char in word_counter):
                    continue
                
                # 3. 각 문자의 개수가 퍼즐에서 사용 가능한 개수를 초과하지 않아야 함
                if all(word_counter[char] <= puzzle_counter[char] for char in word_counter):
                    count += 1
            
            result_count[central_char] = count
        
        # 최소, 최대 개수 찾기
        min_count = min(result_count.values())
        max_count = max(result_count.values())
        
        # 최소 개수를 만드는 문자들
        min_chars = sorted([char for char, count in result_count.items() if count == min_count])
        # 최대 개수를 만드는 문자들
        max_chars = sorted([char for char, count in result_count.items() if count == max_count])
        
        # 출력
        min_chars_str = ''.join(min_chars)
        max_chars_str = ''.join(max_chars)
        print(f"{min_chars_str} {min_count} {max_chars_str} {max_count}")
        

if __name__ == '__main__':
    # 사전 입력 받기 및 전처리
    word_data = []
    while True:
        word = input().strip()
        if word == '-':
            break
        word_counter = Counter(word)
        word_chars = set(word)
        word_data.append((word, word_counter, word_chars))
    
    # 각 퍼즐판 처리
    while True:
        puzzle = input().strip()
        if puzzle == '#':
            break
        
        puzzle_counter = Counter(puzzle)
        puzzle_chars = set(puzzle)
        
        # 퍼즐로 만들 수 있는 단어들 먼저 필터링
        valid_words_by_central = defaultdict(list)
        
        for word, word_counter, word_chars in word_data:
            # 단어의 모든 문자가 퍼즐에 있는지 확인
            if not word_chars.issubset(puzzle_chars):
                continue
            
            # 각 문자의 개수 확인
            valid = True
            for char, needed in word_counter.items():
                if needed > puzzle_counter[char]:
                    valid = False
                    break
            
            if not valid:
                continue
            
            # 이 단어가 유효하다면, 포함된 각 문자를 중앙에 놓을 때 카운트
            for char in word_chars:
                if char in puzzle_chars:
                    valid_words_by_central[char].append(word)
        
        # 결과 계산
        result_count = {}
        for central_char in puzzle_chars:
            result_count[central_char] = len(valid_words_by_central[central_char])
        
        # 최소, 최대 개수 찾기
        counts = list(result_count.values())
        min_count = min(counts)
        max_count = max(counts)
        
        # 최소/최대 개수를 만드는 문자들
        min_chars = []
        max_chars = []
        
        for char in sorted(puzzle_chars):
            if result_count[char] == min_count:
                min_chars.append(char)
            if result_count[char] == max_count:
                max_chars.append(char)
        
        # 출력
        min_chars_str = ''.join(min_chars)
        max_chars_str = ''.join(max_chars)
        print(f"{min_chars_str} {min_count} {max_chars_str} {max_count}")