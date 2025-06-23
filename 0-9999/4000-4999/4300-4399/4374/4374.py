import re

from collections import defaultdict

def extract_lowercase(text):
    """
    1. 정규식을 활용하여 문자 단위로 단어를 쪼갠다.
    2. 소문자로 변환하여 반환 
    """
    words = re.findall(r'[a-zA-Z]+', text)
    return [word.lower() for word in words]

if __name__ == '__main__':
    
    while True:
        try:
            N = int(input())
            words = defaultdict(int)
            while True:
                line = input()
                
                # 문장 종료
                if line.strip() == 'EndOfText':
                    break
                
                # 공백을 기준으로 문장 -> 단어 쪼개기
                # 단어를 딕셔너리에 추가하여 count
                for word in list(line.split()):
                    word_lst = extract_lowercase(word)
                    
                    if word_lst: 
                        for w in word_lst:
                            words[w] += 1

            result = [k for k, v in words.items() if v == N] 

            # 조건에 맞게 결과 반환 
            if len(result) == 0:
                print('There is no such word.')
            else:
                for s in sorted(result):
                    print(s)
            print()
        except:
            break
