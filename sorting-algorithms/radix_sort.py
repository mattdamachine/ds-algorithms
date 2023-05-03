'''Radix Sort Implementation.
   Time Complexity = O(nw),
   where n is the number of keys, and w is the length of the longest key'''

from functools import reduce

def get_num_digits(A):
    '''Get num of digits in longest integer in list A'''
    m = 0
    for item in A:
        m = max(item, m)
    return len(str(m))

def flatten(A):
    '''flatten into a 1D list'''
    return reduce(lambda x, y: x + y, A)

def radix(A, num_digits):
    for digit in range(0, num_digits):
        B = [[] for i in range(10)]  # list of empty buckets
        for item in A:
            num = (
                item // (10 ** (digit)) % 10
            )  # num is the bucket number that the item will be put intp
            B[num].append(item)
        A = flatten(B)

    return A


if __name__ == "__main__":
    A = [55, 45, 3, 288, 213, 1, 288, 53, 2]
    num_digits = get_num_digits(A)
    A = radix(A, num_digits)
    print(A)

    B = [i for i in range(0, 1000000)]
    B = radix(B, get_num_digits(B))
    print(B[:10], B[-10:])
