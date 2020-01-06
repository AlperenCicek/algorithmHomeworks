class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def addingNewNode(self, inp):
        head = self.head
        if head != None:
            while head.next != None:
                head = head.next
            newNode = Node(inp)
            head.next = newNode
            newNode.prev = head
        else:
            newNode = Node(inp)
            self.head = newNode

    def checkingForSameValue(self, data):
        head = self.head
        check = False
        while head.next != None:
            if head.data == data:
                check = True
            head = head.next
        return check

    def printFunc(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.next

    def divisorFunc(self):
        head = self.head
        while head != None:
            print("\nPositive full divisors of", head.data, "is :")
            for x in range(1, head.data + 1):
                if head.data % x == 0:
                    print(x)
            head = head.next
            

    def UI(self):
        print("How many elements do you want to enter?")
        numberOfNodes = int(input())
        for x in range(1, numberOfNodes + 1):
            print(x,".element:")
            inp = int(input())
            linked.addingNewNode(inp)
        print("\nThese are our nodes:")
        linked.printFunc()
        print("\nWhich number do you want to control?")
        inp = int(input())
        print("\nIs this number in the linked list?:", linked.checkingForSameValue(inp))
        linked.divisorFunc()



linked = LinkedList()
linked.UI()




