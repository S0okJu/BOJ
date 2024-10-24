score = {
    "A+" : 4.5,
    "A0": 4.0,
    "B+" : 3.5,
    "B0": 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F": 0.0
}

def solution():
    res = 0.0
    total = 0.0
    for _ in range(20):
        output_list = input().split()
        if output_list[2] == 'P':
            continue
        res += (float(output_list[1]) * score[output_list[2]])
        total += float(output_list[1])
    print(f"{(res/total):.6f}")

if __name__ == '__main__':
    solution()

