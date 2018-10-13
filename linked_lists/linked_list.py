class LinkedList(Object):
    def __init__(self, head=None):
        self.head = head

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
