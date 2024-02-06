def soln(n, cells):
    """
    returns min len of strip
    required to make all cells
    white
    """

    # find first occrance of B
    m = -1
    for i in range(n):
        if cells[i] == "B":
            m = i
            break

    # find last occrance of B
    k = -1
    for j in range(n - 1, -1, -1):
        if cells[j] == "B":
            k = j
            break

    # print(f"m: {m} and k: {k}")

    if m == -1 and k == -1:
        return 0

    if m == k:
        return 1

    return k - m + 1


t = int(input())

for _ in range(t):
    n = int(input())
    cells = input()
    print(soln(n, cells))