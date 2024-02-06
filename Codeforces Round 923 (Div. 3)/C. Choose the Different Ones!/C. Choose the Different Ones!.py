def soln(a, b, n, m, k):
    '''
    Your task is to determine whether it is possible to choose exactly k/2
    elements from both arrays in such a way that among the chosen elements,
    every integer from 1 to k is included.
    '''
    # print(f"a:{a} \n b:{b}")
    element_count_t = k//2
    element_count_a = 0
    element_count_b = 0

    ha = {}
    hb = {}

    for i,val in enumerate(a):
        ha[val] = i
        
    for i,val in enumerate(b):
        hb[val] = i
    
    for ki in range(1,k+1):

        if ha.get(ki, -1) == -1 and hb.get(ki, -1) == -1:
            return "NO"

        if ha.get(ki, -1) != -1:
            element_count_a += 1
        
        if hb.get(ki, -1) != -1:
            element_count_b += 1

    if element_count_a >= element_count_t and element_count_b >= element_count_t:
        return "YES"

    return "NO"



t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    print(soln(a, b, n, m, k))