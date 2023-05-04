'''Implementation of Max Heap'''
class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]  # Create a new list to store the values with a dummy value "0"
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1) # Float each item into their proper positions

    def __str__(self):
        '''Return a string-representation of the heap'''
        return str(self.heap[1:len(self.heap)])

    def push(self, data):
        '''Add a new item to the heap'''
        self.heap.append(data)  # Add to end of array
        self.__floatUp(len(self.heap) - 1)  # Float up to proper position

    def peek(self):
        '''Return the top most value in the heap (largest)'''
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        '''Remove and return the top most value in the heap'''
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)  # swap the max and the value at the end of the array
            max = self.heap.pop()  # Delete the max
            self.__bubbleDown(1)  # Bubble down the item at index 1 to its proper position
        elif len(self.heap) == 2:  # Only one value in the heap
            max = self.heap.pop()
        else:
            max = False
        return max

    def delete(self, index):
        '''Delete a node at a specified index'''
        self.__swap(index, len(self.heap) - 1)
        self.heap.pop()
        self.__bubbleDown(index)

    def is_empty(self):
        '''Return True if the heap is empty, False otherwise'''
        if len(self.heap) > 1:
            return False
        else:
            return True

    def __swap(self, i , j):
        '''Swap element i in the heap with element j'''
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        '''Float a node up if it is larger than its parent node'''
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:  # if the child is greater than the parent
            self.__swap(index, parent)  # swap them
            self.__floatUp(parent)  # recursively call floatUp on the parent 
    
    def __bubbleDown(self, index):
        '''Bubble a node down if either of its child nodes are greater'''
        left = index * 2  # left child
        right = index * 2 + 1  # right child
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:  # compare to left child
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:  # compare to right child
            largest = right
        if largest != index:  # the value must continue to be bubbled down
            self.__swap(index, largest)  # swap the values
            self.__bubbleDown(largest)  # continue bubbling

    def heap_sort(self):
        '''Sort the nodes in a heap by utilizing the heap's pop method.
           Sorted order is built backwards from the largest node.'''
        n = len(self.heap)
        sorted = []
        for i in range(n, 1, -1):
            sorted.insert(0, self.heap[1])
            self.pop()
        return sorted

def main():
    # Build a max heap from an array of integers
    heap = MaxHeap([10, 20, 30, 50, 60, 70, 80, 90])
    print(heap)

    # Add an element to the heap
    heap.push(25)
    print(heap)

    # Peek at the top value of the heap
    print(heap.peek())

    # Remove the top value of the heap
    print(heap.pop())
    print(heap)

    # Delete a node at a specific index
    heap.delete(3)
    print(heap)

    # Return whether or not the heap is empty
    print(heap.is_empty())

    # Sort the elements in the heap
    print(heap.heap_sort())

if __name__ == '__main__':
    main()