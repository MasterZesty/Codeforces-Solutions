def soln(a, n):
    '''
    Vasya has two hobbies — adding permutations†
    to arrays and finding the most frequently occurring element. Recently, he found an array a
    and decided to find out the maximum number of elements equal to the same number in the array a
    that he can obtain after adding some permutation to the array a.

    More formally, Vasya must choose exactly one permutation p1,p2,p3,…,pn
    of length n , and then change the elements of the array a
    according to the rule ai:=ai+pi. After that, Vasya counts how many times each number occurs in the array a
    and takes the maximum of these values. You need to determine the maximum value he can obtain.

    † A permutation of length n is an array consisting of n distinct integers from 1 to n
    in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2
    appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).
    '''
    from bisect import bisect_right

    distinct_nums = sorted(set(a))
    k = n
    res = 1
    
    for i in range(len(distinct_nums)):
        end_num  = distinct_nums[i] + k - 1
        count = bisect_right(distinct_nums, end_num, i) - i
        res = max(res, count)

    return res



t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(soln(a, n))


# INPUT = "input.txt"
# OUTPUT = "output.txt"

# with open(INPUT) as i, open(OUTPUT) as o:
#     lines_i = [line.rstrip() for line in i]
#     lines_o = [line.rstrip() for line in o]
#     # print(lines_i)
#     # print(lines_o)

#     t = int(lines_i[0])
#     c = 1
#     o = 0
#     print(f"output \t| expected")
#     for l in range(t):
#         n = int(lines_i[c])
#         a = list(map(int, lines_i[c+1].split(" ")))
#         print(f"{soln(a, n)} \t| {lines_o[o]}")
#         c += 2
#         o += 1
