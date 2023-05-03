"""
Merge Sort
Divide and conquer algorithm - breaks down problem into subproblems in a recursive fashion
O(n*log(n))
1. Split array in half
2. Call Merge sort on each half to sort them recursively 
3. Merge both sorted halves into one sorted array  
"""

def merge_sort(A):
    # Base case for an array of size 1
    if len(A) < 2:
        return

    # split array in half
    left_A = A[0 : len(A) // 2]
    right_A = A[len(A) // 2 :]

    # recursion
    merge_sort(left_A)
    merge_sort(right_A)

    i, j, k = 0, 0, 0  # left index, right index, merged index

    # merge
    while i < len(left_A) and j < len(right_A):
        if left_A[i] < right_A[j]:
            A[k] = left_A[i]
            i += 1
        else:
            A[k] = right_A[j]
            j += 1
        k += 1

    # a special case where the right array is done but there are still elements in the left array that need to be sorted
    while i < len(left_A):
        A[k] = left_A[i]
        i += 1
        k += 1
    # same thing as before but for the right array
    while j < len(right_A):
        A[k] = right_A[j]
        j += 1
        k += 1


""" Iterative implementation of Merge Sort """

def merge_sort_it(A):
    '''Iteratively sort sublist `A[low…high]` using a temporary list'''
    low = 0
    high = len(A) - 1

    # utilize a temp list to sort A
    temp = A.copy()

    # divide the list into blocks of size 'm'
    # m = [1, 2, 4, 8, 16...]
    m = 1
    while m <= high - low:
        # for m = 1, i = [0, 2, 4, 6, 8...]
        # for m = 2, i = [0, 4, 8, 12...]
        # for m = 4, i = [0, 8, 16...]
        # ...

        for i in range(low, high, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            merge(A, temp, frm, mid, to)

        m = 2 * m

def merge(A, temp, frm, mid, to):
    '''Merge two sorted sublists 'A[frm...mid]' and 'A[mid+1...to]'''
    k = frm
    i = frm
    j = mid + 1

    # loop till no elements are left in the left and right runs
    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1

        k += 1

    # copy remaining elements
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k += 1
        i += 1

    # no need to copy the second half (since the remaining items are already in their
    # correct position in the temp array

    # copy back to the original list to reflect sorted order
    for i in range(frm, to + 1):
        A[i] = temp[i]


if __name__ == "__main__":
    A = [6, 4, 5, 3, 2, 1]
    print("Original Array: ", A)
    merge_sort(A)
    print("Modified Array: ", A)
