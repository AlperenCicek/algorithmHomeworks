class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printFunc(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.next

    def addingNewNode(self, data):
        head = self.head
        if head != None:
            while head.next != None:
                head = head.next
            newNode = Node(data)
            head.next = newNode
            newNode.prev = head
        else:
            newNode = Node(data)
            self.head = newNode

    def convertingNodesToArray(self):
        head = self.head
        array = []
        while head != None:
            array.append(head.data)
            head = head.next
        return array

    def recursiveBubbleSort(self, array, i):
        print("Processing Recursive Sorting:", array)
        if i < len(array):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            linked.recursiveBubbleSort(array, i + 1)
        else:
            print("After Recursive Sorting:", array)

    def iterativeBubbleSort(self):
        array = linked.convertingNodesToArray()
        print("Before Iterative sorting:",array)
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print("After Iterative sorting:",array)

    def UI(self):
        print("How many nodes do you want to enter?")
        numberOfNodes = int(input())
        for x in range(1, numberOfNodes + 1):
            print(x,".element:")
            inp = int(input())
            linked.addingNewNode(inp)
        print("\nThese are our nodes:")
        linked.printFunc()
        print("\nWhich method do you want to sort? (Recursive: 0 / Non-Recursive: 1):")
        inp = int(input())
        if inp == 0:
            linked.recursiveBubbleSort(linked.convertingNodesToArray(), 0)
        elif inp == 1:
            linked.iterativeBubbleSort()

linked = LinkedList()
linked.UI()

