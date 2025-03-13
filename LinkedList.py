import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def addNode(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = Node(data)

    def removeNode(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.next.data == data:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next

class MainProgram:
    ll = LinkedList()
    for i in range(22):
        f = random.randint(1, 1900)
        ll.addNode(f)

    ll.printList()