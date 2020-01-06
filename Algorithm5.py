import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

class Weight:
    def __init__(self, weight):
        self.weight = weight
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.weightHead = None

    def scatting(self, nodeA, ax):
        ax.scatter(nodeA.x, nodeA.y, color = 'r')

    def lining(self, nodeA, nodeB, weight):
        plt.plot([nodeA.x, nodeB.x], [nodeA.y, nodeB.y])
        plt.text((nodeA.x + nodeB.x) / 2, (nodeA.y + nodeB.y) / 2, weight)

    def showWeights(self):
        weightHead = self.weightHead
        print("\nPATH IS LIKE THAT:\n")
        while weightHead != None:
            print(weightHead.weight)
            weightHead = weightHead.next

    def addingNewNode(self, dataX, dataY):
        head = self.head
        if head != None:
            while head.next != None:
                head = head.next
            newNode = Node(dataX, dataY)
            head.next = newNode
            newNode.prev = head
        else:
            newNode = Node(dataX, dataY)
            self.head = newNode
        print("X:", dataX, "Y:", dataY)
        
    
    def draw(self):
        head1 = self.head
        _, ax = plt.subplots(figsize = (4, 4))
        while head1 != None:
            head2 = self.head
            while head1.x != head2.x and head1.y != head2.y:
                head2 = head2.next
            while head2 != None:
                if head1 != head2:
                    weightHead = self.weightHead
                    randomWeight = random.randrange(1, 21)
                    if weightHead != None:
                        while weightHead.next != None:
                            weightHead = weightHead.next
                        newWeight = Weight(randomWeight)
                        weightHead.next = newWeight
                    else:
                        newWeight = Weight(randomWeight)
                        self.weightHead = newWeight
                    LinkedList.lining(self, head1, head2, newWeight.weight)
                head2 = head2.next
            head1 = head1.next
        samplePath.showWeights()
        plt.show()

    def LocationOfNodeOnCylinder(self, numberOfNodes):
        for x in range(numbersOfNodes):
            yPoint = random.randrange(-100, 101)
            randomNumber = random.randrange(0, 2)
            if randomNumber % 2 == 0:
                xPoint = - (10000 - yPoint ** 2) ** (1 / 2)
            else:
                xPoint = (10000 - yPoint ** 2) ** (1 / 2)       
            LinkedList.addingNewNode(self, xPoint, yPoint)
        
    def UI(self):
        print("How many nodes do you want to enter?")
        global numbersOfNodes
        numbersOfNodes = int(input())
        samplePath.LocationOfNodeOnCylinder(numbersOfNodes)
        samplePath.draw()


samplePath = LinkedList()
samplePath.UI()


