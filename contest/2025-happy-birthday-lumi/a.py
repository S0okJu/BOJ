
def calcH(V, m, r, g, b):
    if V == r:
        H = 60 * ((g - b) / (V - m))
    elif V == g:
        H = 120 + 60 * ((b - r) / (V - m))
    elif V == b:
        H = 240 + 60 * ((r - g) / (V - m))

    if H < 0:
        H += 360

    return H

if __name__ == '__main__':
    
    hlo,hhi = list(map(int, input().split()))
    slo,shi = list(map(int, input().split()))
    vlo,vhi = list(map(int, input().split()))
    rgb= list(map(int, input().split()))
    r,g,b = rgb
    M = max(rgb)
    m = min(rgb)
    # print(m)
    
    V = M  
    S = 0 if V == 0 else 255 * (V - m) / V  
    H = calcH(V, m, r, g, b) 
    if (hlo <= H <= hhi) and (slo <= S <= shi) and (vlo <= V <= vhi):
        print('Lumi will like it.')
    else:
        print('Lumi will not like it.')
