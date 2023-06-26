from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return " > ".join(values)

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length 
    
    def add(self, value): # Add/ insert value inside the linked list
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self.tail
    
    def generate(self, n, min_value, max_value):
        for i in range(n):
            self.add(randint(min_value, max_value))
        # return self