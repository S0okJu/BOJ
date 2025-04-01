import sys 
input = sys.stdin.readline

def solution(N, bundles, ones):
    target = N 
    
    # 묶음과 낱개 중에서 싼 제품을 사용한다.
    min_bundle = min(bundles)
    min_ones = min(ones)
    
    result = 0
    
    while target > 0:
        
        # 6개 미만이라도 묶음 가격이 더 쌀 수 있음 
        if target < 6:
            if min_bundle < (target * min_ones):
                result += min_bundle
            else:
                result+=(target * min_ones)
            break 
        else:
            # 묶음으로 수행하는 경우 vs 개별로 사용하는 경우
            bundle_cnt = (target//6)
            target = target % 6
            # 묶음이 더 싸다면 묶음 가격으로 측정 
            if bundle_cnt* min_bundle < bundle_cnt * 6 * min_ones:
                result += (bundle_cnt* min_bundle)
            else:
                result += bundle_cnt * 6 * min_ones
    
    return result
                    
            
if __name__ == '__main__':
    N, M =map(int,input().split())
    bundles = list()
    ones = list()
    for i in range(M):
        bundle, one = map(int,input().split())
        bundles.append(bundle)
        ones.append(one)
    
    
    print(solution(N,bundles, ones))
        