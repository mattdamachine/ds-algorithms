""" Insertion sort implementation.
A slow sorting algorithm that uses nested loops to sort.
Useful only for small data sets.
Runs in O(n^2) in both instances. """

def insertion_sort(A):
    for i in range(1, len(A)):  # i index starts on the second item of the list
        for j in range(i - 1, -1, -1):  # start from the item to the left of i and move towards 0
            if A[j] > A[j + 1]:  # compare A[j] and A[j+1]
                A[j], A[j + 1] = A[j + 1], A[j]  # have them swap places
            else:
                break
    return A

def insertion_sort2(A):
    # this is a shifting method that will utilize a temp variable (curNum)
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i - 1, -1, -1):
            if A[j] > curNum:
                A[j + 1] = A[j]
                A[j] = curNum
            else:
                break
    return A


if __name__ == "__main__":
    A = [6, 4, 5, 2, 1, 3]
    print("Original Array: ", A)
    insertion_sort(A)
    print("Modified Array: ", A)
