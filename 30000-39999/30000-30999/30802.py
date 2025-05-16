
def shirt(t, shirts):
    cnt = 0
    for shirt in shirts:
        if shirt % t == 0:
            cnt = cnt + int(shirt/t)
        else: 
            cnt = cnt + int(shirt / t) + 1
    return cnt 

# n 전체 참가자
# p 펜의 묶음 수 
def pen(n, p):
    bundle = n / p 
    piece = n % p
    return int(bundle), piece

if __name__ == "__main__":
    n = input()
    sh = input().split() 
    shirts = [int(x) for x in sh]
    t, p = input().split()
    
    print(shirt(int(t),shirts))
    
    bundle, piece = pen(int(n),int(p))
    print(f"{bundle} {piece}")
    