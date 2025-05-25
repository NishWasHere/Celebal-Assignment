rows = 5
print("Lower Triangular Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


print("\nUpper Triangular Pattern:")
for i in range(rows):
    for j in range(i):
        print(" ", end=" ")
    for k in range(rows - i):
        print("*", end=" ")
    print()


print("Full Pyramid Pattern:")
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars with a space between them
    for k in range(2 * i - 1):
        print("*", end="")
    print()
