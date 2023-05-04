# Stack implementation using a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        ''' A dummy head node is used to help with edge cases'''
        self.head = Node('head') 
        self.size = 0

    def __str__(self):
        '''Return string representation of the stack'''
        cur = self.head.next
        output = ""
        while cur:
            output += str(cur.value) + "->"
            cur = cur.next
        return output[:-2]

    def __len__(self):
        '''Return the current size of the stack'''
        return self.size

    def isEmpty(self):
        '''Check to see if the stack is empty or not'''
        return self.size == 0

    def peek(self):
        '''Return the top item of the stack (last one that was inserted)'''
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        '''Push a value into the stack'''
        node = Node(value)
        node.next = self.head.next  # Use head.next to move over the dummy node
        self.head.next = node
        self.size += 1

    def pop(self):
        '''Remove and return the top value from the stack'''
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

def is_balanced(string):
    '''Determine if a given string is balanced (does each '(' and '[' have
       a corresponding ')' and ']' respectively
       (example: is_balanced('()[]') -> True
       is_balanced('((]') -> False'''
    stack = Stack()
    for char in string:
        if char in ('(', '['):
            stack.push(char)
        else:
            if stack.isEmpty(): return False
            top = stack.pop()
            if ((top == '[' and char != ']') or (top == '(' and char != ')')):
                return False
    return stack.isEmpty()

def main():
    # Initialize stack
    my_stack = Stack()
    
    # Push elements onto stack
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    print(my_stack)
    
    # Get length of stack
    print(f"Current Size: {len(my_stack)}")

    # Peek at topmost element
    print(f"The last inserted element is {my_stack.peek()}")

    # Remove item from top of stack
    print(f"Successfully popped {my_stack.pop()} from the stack")
    print(my_stack)

    # Use stack to determine whether a string is balanced or not
    print(is_balanced('[[[([])]]]'))

if __name__ == '__main__':
    main()