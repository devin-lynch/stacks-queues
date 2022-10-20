class Node:
    '''
        singly linked list node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    
    def __init__(self):
        self.head = None

    def is_empty(self): # checks if stack is empty!
        if self.head == None:
            return True
        else:
            return False

    
    def __str__(self):
        current_node = self.head
        string = str(current_node)

        while current_node.next:
            string += f' -> {str(current_node.next)}'
            current_node = current_node.next

        return f' [ {string} ] '

    
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    
    def pop(self):
        if self.head == None:
            return None
        else:
            pop_value = self.head.data
            self.head = self.head.next
            return pop_value


    def peek(self):
        # top_node = self.head

        if self.is_empty():
            return None
        else:
            return self.head.data





my_stack = Stack()

my_stack.push(21)
my_stack.push(20)
my_stack.push(9)

print(my_stack)
print(my_stack.peek())

my_stack.pop()

print(my_stack)
# my_stack.peek()
