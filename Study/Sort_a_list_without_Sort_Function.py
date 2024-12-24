l = [23, 4, 2, 5, -1]
# Outer loop iterates through the entire list
for i in range(0, len(l)):
    # Inner loop compares the current element with the subsequent elements
    for j in range(i + 1, len(l)):
        # If the current element is greater than or equal to the next element
        if l[i] >= l[j]:
            # Swap the elements
            l[i], l[j] = l[j], l[i]

print(l)
