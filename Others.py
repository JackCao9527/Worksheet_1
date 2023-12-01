Print the following pattern using loops:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 (Question)

for n in range(2, 102):
    for i in range(1, n):
        print (i, end=" ")
    print()


Write a program that uses a for loop in order to print the following reverse number pattern
100 99 98 ... 1
99 98 97 ... 1 (Quetion)

for n in range(100, 0, -1):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()

Find the loop the prints the following pattern:
1 2 3 4 5 6 7 8 9 10
2 3 4 5 6 7 8 9 10 11
3 4 5 6 7 8 9 10 11 12
4 5 6 7 8 9 10 11 12 13
5 6 7 8 9 10 11 12 13 14 (Question)

for i in range(1, 6):
    for n in range(i, i + 10):
        print(n, end=" ")
    print()


(Display patterns) Write a function to display a pattern as follows:
1
2 1
3 2 1
.........
n n-1 ... 3 2 1

The function header is
def displayPattern(n):
Write a test program that prompts the user to enter a number n and invokes
displayPattern(n) to display the pattern. (Question)

def display_pattern(n):
    for j in range(1, n + 1):
        for i in range(j, 0, -1):
            print(i, end=" ")
        print()
n = int(input("Please enter a number: "))
display_pattern(n)


(Display a pyramid) Write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid, as
shown in the following sample run:
Enter the number of lines: 7
                                1
                              2 1 2
                            3 2 1 2 3
                          4 3 2 1 2 3 4
                        5 4 3 2 1 2 3 4 5
                      6 5 4 3 2 1 2 3 4 5 6
                    7 6 5 4 3 2 1 2 3 4 5 6 7 (Question)

n = int(input("Please enter a number: "))
for j in range(1, n + 1):
    spaces_count1 = (n - j) * 2
    print(" " * spaces_count1, end="")
    for i in range(j, 0, -1):
        print(i, end=" ")
    for i in range(2, j + 1):
        print(i, end=" ")
    print()


distances = input("Please enter the distances: ").split(", ")
distances = [int (x) for x in distances]
cumulative_distances = [0]
for distance in distances:
    cumulative_distances.append(cumulative_distances[-1] + distance)
for i in range(len(cumulative_distances)):
    row = []
    for j in range(len(cumulative_distances)):
        row.append(abs(cumulative_distances[i] - cumulative_distances[j]))
    print(' '.join(map(str, row)))
