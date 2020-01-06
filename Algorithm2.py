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
            head = head.prev

    def addingNewNode(self, data):
        head = self.head
        if head != None:
            newNode = Node(data)
            head.next = newNode
            newNode.prev = head
            self.head = newNode
        else:
            newNode = Node(data)
            self.head = newNode

    def convertingNodesToArray(self):
        head = self.head
        array = []
        while head != None:
            array.append(head.data)
            head = head.prev
        return array

    def recursiveSelectionSort(self, array, i):
        print("Processing Recursive Sorting:",array)
        if i < len(array):
            min = i
            for j in range(i + 1, len(array)):
                if array[min] > array[j]: 
                    min = j 
            array[i], array[min] = array[min], array[i]
            linked.recursiveSelectionSort(array, i+1)
        else:
            print("After Recursive Sorting:",array)
        

    def iterativeSelectionSort(self):
        array = linked.convertingNodesToArray()
        print("\nBefore Iterative Sorting:",array)
        for i in range(0, len(array) - 1): 
            min = i 
            for j in range(i+1, len(array)): 
                if array[min] > array[j]: 
                    min = j 
                       
            array[i], array[min] = array[min], array[i]
        print("After Iterative Sorting:",array)
        


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
            linked.recursiveSelectionSort(linked.convertingNodesToArray(), 0)
        elif inp == 1:
            linked.iterativeSelectionSort()

linked = LinkedList()
linked.UI()

