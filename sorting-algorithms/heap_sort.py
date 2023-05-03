'''Implementation of heap sort'''

def heapify(array, heap_size, i):
    ''' Value at i is compared against its children 
        and swapped to maintain heap integrity'''
    left = i * 2
    right = i * 2 + 1

    largest = i

    # Compare value at i with left child
    if (left < heap_size) and (array[left] > array[i]):
        largest = left

    # Compare value at i with right child
    if (right < heap_size) and (array[right] > array[largest]):
        largest = right

    # swap i with largest value and continue to heapify
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, heap_size, largest)

def build_maxheap(array):
    heap_size = len(array)
    # We only need to heapify the non-leaf nodes
    for i in range(heap_size // 2, 0, -1):
        heapify(array, heap_size, i)

def heap_sort(array):
    build_maxheap(array)  # Build heap from array
    heap_size = len(array)

    # swap last element with first and heapfiy the new first node
    for i in range(heap_size - 1, 1, -1):
        array[1], array[i] = array[i], array[1]
        heapify(array, i, 1)


if __name__ == "__main__":
    A = [None, 3, 6, 1, 2, 4, 5, 7]
    print("Original Array: ", A[1:])
    heap_sort(A)
    print("Modified Array: ", A[1:])
