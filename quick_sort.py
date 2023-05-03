"""
Quick Sort
Another divide and conquer algorithm
Fastest comparison-based sort for arrays
Worst case running time: O(n^2)
Best and average case: O(n*log(n))

1. Choose pivot element (usually last or random)  (this is what will determine how quickly the algo can run)
2. Store elements less than pivot in left subarray
   Store elements greater than pivot in right subarray
   * Note - this is an in-place sorting algo, so no new auxillary arrays will be created. 
   Instead, we'll just use pointers to section off the array.
3. Call quick sort recursively on both the left and right subarray 
"""

def quick_sort(A, left, right):
    if left < right:  # array must have two or more elements to call these
        partition_index = partition(A, left, right)
        quick_sort(A, left, partition_index - 1)  # left subarray
        quick_sort(A, partition_index + 1, right)  # right subarray

def partition(A, left, right):
    i = left
    j = right - 1
    pivot = A[right]

    # i will continue to look for elements that are bigger than the pivot element
    # j will continue to look for elements that are smaller than the pivot element
    # until i and j cross. Then we will swap A[i] with the pivot element
    while i < j:
        while i < right and A[i] < pivot:
            i += 1
        while j > left and A[j] >= pivot:
            j -= 1
        if i < j:  # only swap here if i and j did not cross yet
            A[i], A[j] = A[j], A[i]

    if A[i] > pivot:
        A[i], A[right] = A[right], A[i]

    return i  # this is where we will split the array to recall quicksort

def kth_smallest(A, left, right, k):
    '''Finds the kth position (of the sorted array) in a given unsorted array
       Similar to quicksort, except we only have to look at one side once we partition the array
       O(n) average time if pivot is selected randomly'''
    
    # if k is smaller than number of elements in array
    if k > 0 and k <= right - left + 1:
        # Partition the array and get position of pivot
        index = partition(A, left, right)

        # if position is the same as k
        if (index - left) == (k - 1):
            return A[index]

        # if position is more, recursively call for left subarray
        if (index - left) > (k - 1):
            return kth_smallest(A, left, index - 1, k)

        # Else recursively call for right subarray
        return kth_smallest(A, index + 1, right, k - index + left - 1)


if __name__ == "__main__":
    A = [17, 14, 15, 6, 9, 4, 11]
    print("Original Array: ", A)
    quick_sort(A, 0, len(A) - 1)
    print("Modified Array: ", A)
