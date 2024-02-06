def soln(n, s):
    '''
    from trace of string s 
    obtain a string
    '''
    arr = [-1 for _ in range(26)]
    ans = []

    for trace in s:
        trace = int(trace)
        for j in range(26):
            if arr[j] + 1 == trace:
                ans.append(chr(ord('a')+j))
                arr[j] = trace
                break

    # print(f"ans: {ans}")
    return "".join(ans).replace(" ", "")


t = int(input())

for _ in range(t):
    n = int(input())
    s = input().replace(" ", "")
    print(soln(n, s))