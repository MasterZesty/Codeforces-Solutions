def soln(a, b):
    '''
    Help Bob determine if he can obtain some other 
    rectangle, or if he is just wasting his time.
    '''
    # print(f"for {a}x{b} ->")

    rect0 = [a, b]
    rect1 = [a/2, 2*b]
    rect2 = [2*a, b/2]

    rect0.sort()
    rect1.sort()
    rect2.sort()

    # print(f"{rect0} \n {rect1} \n {rect2}")

    if (a, b) == (1, 1):
        return "No"

    if rect0 == rect1 and rect0 == rect2:
        return "No"

    if rect0 != rect1 and rect0 != rect2:
        if int(rect2[0]) == rect2[0] and int(rect2[1]) == rect2[1]:
            return "Yes"

        if int(rect1[0]) == rect1[0] and int(rect1[1]) == rect1[1]:
            return "Yes"

    if rect0 == rect1 and rect0 != rect2:
        if int(rect2[0]) == rect2[0] and int(rect2[1]) == rect2[1]:
            return "Yes"

    if rect0 == rect2 and rect0 != rect1:
        if int(rect1[0]) == rect1[0] and int(rect1[1]) == rect1[1]:
            return "Yes"

    return "No"


t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split(" ")))
    print(soln(a, b))


# INPUT = "input.txt"
# OUTPUT = "output.txt"

# with open(INPUT) as i, open(OUTPUT) as o:
#     lines_i = [line.rstrip() for line in i]
#     lines_o = [line.rstrip() for line in o]
#     # print(lines_i)
#     # print(lines_o)

#     t = int(lines_i[0])
#     c = 1
#     print(f"input \t| output \t| expected")
#     for l in range(t):
#         a, b = list(map(int, lines_i[c].split(" ")))
#         print(f"{a}x{b} \t| {soln(a, b)} \t| {lines_o[c-1]}")
#         c += 1
