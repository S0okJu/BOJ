from collections import defaultdict

def solution(N: int, words: list) -> int:
    grouped = defaultdict(list)

    for word in words:
        first_char = word[0]
        grouped[first_char].append(word)
        
    for key in grouped:
        grouped[key] = sorted(grouped[key], key=lambda x: (x, len(x)))

    prefix_count = 0

    for alphabet, values in grouped.items():
        values_len = len(values)
        for prefix_idx in range(values_len - 1):
            is_prefix = False
            for target_idx in range(prefix_idx + 1, values_len):
                if values[target_idx].startswith(values[prefix_idx]):
                    is_prefix = True
                    break
            if is_prefix:
                prefix_count += 1

    return N - prefix_count


if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    print(solution(N, words))
