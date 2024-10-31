MOD = 900528

def main():
    pos = {}
    cnt = 0

    key = input().strip()
    for char in key:
        cnt += 1
        pos[char] = cnt

    data = input().strip()
    length = len(data)
    ans = 0
    g = 1

    for i in range(length - 1, -1, -1):
        ans = (ans + g * pos[data[i]]) % MOD
        g = (g * cnt) % MOD

    print(ans)

if __name__ == "__main__":
    main()
