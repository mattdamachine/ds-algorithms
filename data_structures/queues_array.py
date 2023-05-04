# Circular Array Implementation of a Queue
class Queue:
    def __init__(self, capacity):
        '''The front index will be for deleting. The rear index will be for inserting'''
        self.front = self.size = self.rear = 0
        self.Q = [None] * capacity  # list representation of the queue
        self.capacity = capacity

    def __str__(self):
        '''Return string representation of queue'''
        output = []
        for item in self.Q:
            output.append(str(item))
        return '->'.join(output)

    def is_full(self):
        '''Queue is full when size becomes equal to the capacity'''
        return self.size == self.capacity

    def is_empty(self):
        '''Return whether or not the queue is empty'''
        return self.size == 0

    def enqueue(self, value):
        '''Add an item to the queue. This will update rear index and size'''
        if self.is_full():
            raise Exception("Queue is Full")
        self.Q[self.rear] = value  # Insert the value at the rear
        self.rear = (self.rear + 1) % self.capacity  # Update the rear index
        self.size += 1  # Update the size

    def dequeue(self):
        '''Remove an item from queue. This will update front index and size'''
        if self.is_empty():
            raise Exception("Queue is empty")
        remove = self.Q[self.front]
        self.Q[self.front] = None  # Delete the value at the front
        self.front = (self.front + 1) % self.capacity  # Update the front index
        self.size -= 1  # Update the size
        return remove

def main():
    # Initialize Queue with specified capacity
    my_queue = Queue(4)

    # Add items to queue
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)

    print(my_queue)
    print(my_queue.is_empty())

    # Remove items from queue
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())

    print(my_queue)

    # Verify queue is empty
    print(my_queue.is_empty())

if __name__ == '__main__':
    main()