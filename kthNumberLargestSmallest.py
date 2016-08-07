def typeZeroQuery(arr, X, K):
    n = len(arr)
    i = 0
    
    while i < n:
        if arr[i] == X:
            break
    
    if n - i - 1 < K:
        return -1
    
    return arr[i+K]

def typeOneQuery(arr, X, K):
    n = len(arr)
    i = n - 1
    
    while i >= 0:
        if arr[i] == X:
            break
    
    if  K > i:
        return -1
    
    return arr[i-K]

def kthNumberLargestSmallest(arr, X, k, type):
    if arr == None or len(arr) == 0 or len(arr) <= k:
        return -1
    
    if type == 0:
        return typeZeroQuery(arr, X, k)
    
    if type == 1:
        return typeOneQuery(arr, X, k)

    
if __name__ == "__main__":
    N, Q = map(lambda x: int(x), raw_input().split(" "))
    arr = map(lambda x: int(x), raw_input().split(" "))
    
    results = []
    
    for i in range(Q):
        X, K, type = map(lambda x: int(x), raw_input().split(" "))
        results.append(kthNumberLargestSmallest(arr, X, K, type))
    
    
    for r in results:
        print r