class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queues use a FIFO (First-in First-out) ordering. Think of a line at a grocery store.
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        '''Return a string representation of Queue'''
        cur_node = self.head
        output = []
        while cur_node:
            output.append(str(cur_node.data))
            cur_node = cur_node.next
        return '->'.join(output)

    def is_empty(self):
        '''Check whether the queue is empty or not'''
        return self.head is None

    def enqueue(self, data):
        '''Add a new node onto the back of the queue'''
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        '''Remove a node from the front of the queue'''
        if self.is_empty():
            raise Exception("Error: Queue is empty")
        remove = self.head
        cur_node = self.head.next
        self.head = cur_node
        return remove.data


def main():
    # Initialize Queue
    my_queue = Queue()

    # Add items to queue
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print(my_queue)

    # Check if queue is empty
    print(my_queue.is_empty())

    # Remove items from queue
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())

    print(my_queue.is_empty())

if __name__ == '__main__':
    main()