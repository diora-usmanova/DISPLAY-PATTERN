# DISPLAY PATTERN
def displayPattern(n):
    n = eval(input("Enter a number "))

    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            print(j if j <= i else " ", end=" ")
        print()

displayPattern('n')


