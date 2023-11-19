def modify_string(n,k,s):
    countA = 0
    countB = 0

    for i,c in enumerate(s):
        if c == 'A':
            countA += 1
        
        if c == 'B':
            countB += 1

    targetB = k

    print(f'count A : {countA} count B {countB} target B {targetB}')

    if targetB == countB:
        return 0
    
    if targetB < countB:
        return countB - targetB

    if targetB > countB:
        return targetB - countB

    return -1


# test_cases = int(input())

# for _ in test_cases:
#     n, k = list (map(int, input().split(' ')) )

#     s= input()

#     modify_string(n,k,s)

# 5
# 5 2
# AAABB

# 5 3
# AABAB

# 5 0
# BBBBB

# 3 0
# BAA

# 10 3
# BBBABBBBAB

print(modify_string(10,3,'BBBABBBBAB'))
