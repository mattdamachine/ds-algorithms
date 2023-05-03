''' O(q + n) where q is the range of possible elements
    and n is the number of elements'''
def counting_sort(A):
    num = max(A)
    output = [0 for i in range(len(A))]
    counts = [0 for i in range(num + 1)]

    for item in A:  # count how many instances of each num in array
        counts[item] += 1

    # scan through the array so counts[i] contains # of keys < i
    # this tells us the first index of the output array to put items with key i
    total = 0
    for i in range(len(counts)):
        c = counts[i]
        counts[i] = total
        total = total + c

    # write the items in A to the output array based on the sums we gathered from counts
    for i in range(len(A)):
        output[counts[A[i]]] = A[i]
        counts[A[i]] += 1  # increment so that elements won't collide when adding to output

    return output


if __name__ == "__main__":
    A = [6, 7, 3, 0, 3, 1, 5, 0, 3, 7]
    print("Original Array: ", A)
    B = counting_sort(A)
    print("Modified Array: ", B)
