class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes=None):
        self.head = node()  # points to first element
        if nodes is not None:  # Creates a new linked list from a given set of data (nodes)
            new_node = node(nodes[0])
            self.head = new_node
            for item in nodes:
                new_node.next = node(item)
                new_node = new_node.next

    def __str__(self):
        ''' Return the contents of the LL in a human-readable string.'''
        output = []  # List to keep track of the elements in the linked list
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            output.append(cur_node.data)
        return "->".join(str(x) for x in output)
    
    def __len__(self):
        '''Return length of LL as int'''
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

    def pop_front(self):
        '''Removes an item from the front of the list'''
        if self.empty():
            print("Error: List is empty")
            return
        cur_node = self.head
        cur_node = cur_node.next
        self.head = cur_node

    def pop_back(self):
        '''Removes an item from the back of the list'''
        if self.empty():
            print("Error: List is empty")
            return
        cur_node, last_node = self.head, self.head
        while cur_node.next is not None:
            last_node = cur_node
            cur_node = cur_node.next
        last_node.next = None

    def insert(self, data, index):
        '''Insert a node at a given index'''
        if index >= len(self):
            print('ERROR: Index out of range')
            return
        new_node = node(data)
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                new_node.next = cur_node
                last_node.next = new_node
                return
            cur_idx += 1

    def append(self, data):
        '''Append an item to the end of list'''
        new_node = node(data)
        cur = self.head
        while cur.next != None:  # Traverse through the list until we reach the last node.
            cur = cur.next      # We know we've reached the end because the last node will point to None
        cur.next = new_node     # Point the current last node to the new node

    def append_list(self, list):
        '''Append a given list onto the end of the linked list'''
        cur = self.head
        while cur.next is not None:  # traverse LL
            cur = cur.next

        new_node = node(list[0])  # create node from first item in input list
        cur.next = new_node

        # append each item from input list onto end of LL
        for i in range(1, len(list)):
            new_node.next = node(list[i])
            new_node = new_node.next

    def get_front(self):
        '''Return the element at the beginning of the list'''
        if self.empty():
            print("Error: List is empty")
            return
        return self.head.next.data

    def get_back(self):
        '''Return the element at the end of the list'''
        if self.empty():
            print("Error: List is empty")
            return
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node.data

    def get(self, index):
        '''Return data from a node at a specific index position'''
        if index >= len(self):  # Check to make sure the index is within range of the list
            print('ERROR: Index out of range')
            return None
        cur_idx = 0  # Keep track of the index while we iterate through the list
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            else:
                cur_idx += 1

    def erase(self, index):
        ''' Once we find the index of the node that we want to erase, we will take the pointer
        from the last_node and point it to the next essentially skipping over the node that should
        be deleted '''
        if index >= len(self):
            print('ERROR: Index out of range')
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            prev_node = cur_node  # prev will be right behind current node
            cur_node = cur_node.next
            if cur_idx == index:
                # prev node points to the next node after cur (skipping cur)
                prev_node.next = cur_node.next
                return
            cur_idx += 1

    def remove_value(self, value):
        '''Removes the first item in the list with the specified value'''
        cur_node = self.head
        cur_idx = 0
        while cur_idx < len(self):
            cur_node = cur_node.next
            if cur_node.data == value:
                self.erase(cur_idx)
                return
            cur_idx += 1
        print("Error: Value does not exist in list")
        return

    def empty(self):
        '''Return a bool if the list is empty or not'''
        cur_node = self.head
        if cur_node.next is None:
            return True
        else:
            return False

    def reverse_list(self):
        '''Reverse and print a linked list using python reverse function'''
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        elems.reverse()
        new_list = LinkedList(elems)
        return new_list

    def reverse_list_2pointers(self):
        prev, curr = None, self.head  # the prev pointer will keep track of the reverse direction
        while curr:  # Cycle through the list
            nxt = curr.next  # Store the next in a temp variable so we don't lose it
            curr.next = prev  # Reverse the direction of next
            prev = curr  # advance prev one node to the right
            curr = nxt  # advance curr variable one to the right


        # Return the list of nodes after reversal
        elems = []
        while prev.next:
            elems.append(prev.data)
            prev = prev.next
        return '->'.join(str(x) for x in elems)

    def is_palindrome(self):
        '''Check to see if the linked list is a palindrome using python built-in reverse method'''
        elems = []  # List to keep track of the elements in the linked list
        rev_elems = []  # List that will later be reversed
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
            rev_elems.append(cur_node.data)
        rev_elems.reverse()
        for i in range(len(rev_elems)-1):
            if rev_elems[i] != elems[i]:
                return False
        return True

    def is_palindrome_stack(self):
        '''Using a stack, check to see if a linked list is a palindrome'''
        stack = []

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            stack.append(cur_node.data)

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            last_node = stack.pop()

            if cur_node.data != last_node:
                return False
            
        return True

def find_intersection(listA, listB):
    '''Given two intersecting linked lists,
       find the value at the point at which they intersect'''
    # Initialize the pointers for each list
    a = listA.head
    b = listB.head
    while a != b:
        # If either pointer hits the end of the list, have it switch to the other list and begin
        # another traversal.
        # If not at the end, have the pointer traverse through the list
        a = listB.head if a is None else a.next
        b = listA.head if b is None else b.next
        # By switching heads, the difference in length is countered.
        # On the second traversal, they either hit or miss.
        # If they meet, they will both be equal and we can return that value.
        # If not, they will both equal None and will still break the loop
    return a

def merge_two_lists(list1, list2):
        '''Merge two sorted linked lists in-place by rearranging 
           their pointers (not creating a new list)'''
        l1 = list1.head.next
        l2 = list2.head.next

        # Initialize dummy head and temp (temp will traverse list) (value here is arbitrary)
        dummy = temp = node(0)
        while l1 is not None and l2 is not None:
            if l1.data < l2.data:
                temp.next = l1  # Point temp to lesser value
                l1 = l1.next  # Advance list1 to next value
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next  # Advance the temp variable
        temp.next = l1 or l2  # Add whatever is remaining from the longer linked list
        # return dummy.next  # Return the merged list

        # Display the merged list back to the user
        elems = []
        while dummy.next:
            dummy = dummy.next
            elems.append(dummy.data)
        return elems


def main():
    # Create Linked list from python list object
    myLinkedList = LinkedList([1, 3, 7, 2, 7, 3, 1])
    print(myLinkedList)
    
    # Pop first item from LL
    myLinkedList.pop_front()
    print(myLinkedList)

    # Pop last item from LL
    myLinkedList.pop_back()
    print(myLinkedList)

    # Insert an item into LL at specified index
    myLinkedList.insert(4, 1)
    print(myLinkedList)

    # Append item to the end of LL
    myLinkedList.append(6)
    print(myLinkedList)

    # Get length of LL
    print(len(myLinkedList))

    # Return element at beginning of LL
    print(myLinkedList.get_front())

    # Return element at end of LL
    print(myLinkedList.get_back())

    # Return data from node at given index
    print(myLinkedList.get(2))

    # Remove item in LL with specified value
    myLinkedList.remove_value(4)
    print(myLinkedList)

    # Check to see if LL is empty
    print(myLinkedList.empty())

    # Check to see if LL is palindrome
    print(myLinkedList.is_palindrome_stack())

if __name__ == '__main__':
    main()



