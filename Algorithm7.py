class Node:
    def __init__(self, weight, base, power):
        self.data = str(weight) + "x" + str(base) + "^" + str(power)
        self.weight = weight
        self.base = base
        self.power = power
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
 
    def printFunc(self):
        head = self.head
        while head != None:
            print("Weight:", head.weight, "Base:", head.base, "Power:", head.power)
            print("Result: ",head.data)
            head = head.next

    def splitTheWord(self):
        file = open("text.txt","r")

        for line in file:
            fields = line.split(" ")
            
            weight = fields[0]
            base = fields[1]
            power = fields[2]
            head = self.head
            if head != None:
                while head.next != None:
                    head = head.next
                newNode = Node(weight, base, power)
                head.next = newNode
            else:
                newNode = Node(weight, base, power)
                self.head = newNode
                
        file.close()

linked = LinkedList()
linked.splitTheWord()
linked.printFunc()