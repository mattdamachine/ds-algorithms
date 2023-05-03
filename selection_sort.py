"""
Selction Sort
* simple sorting algorithm with O(n^2) running time
* works by finding the smallest element in a list and then organizing incrementally from there
* uses pointers to aid in swapping the elements 
"""

def selection_sort(A):
    for i in range(0, len(A) - 1):
        cur_min_idx = i
        for j in range(
            i + 1, len(A)
        ):  # Loop to find the smallest element in the list A[i+1:]
            if A[j] < A[cur_min_idx]:
                cur_min_idx = j
        A[i], A[cur_min_idx] = A[cur_min_idx], A[i]  # swap
    return A


if __name__ == "__main__":
    A = [20, 50, 30, 60, 10, 40]
    print("Original Array: ", A)
    selection_sort(A)
    print("Modified Array: ", A)
