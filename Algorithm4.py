class Words:
    def __init__(self, bigWord, smallWord):
        self.bigWord = bigWord
        self.smallWord = smallWord

    def printFunc(self):
        print("Big Word is:", self.bigWord)
        print("Small word is:", self.smallWord)
        print("Big Word has",len(str(self.bigWord)),"letters.")
        print("Small Word has",len(str(self.smallWord)),"letters.")

    def calculatingLocation(self):
        bigWord = str(self.bigWord)
        smallWord = str(self.smallWord)
        array = []
        check = 0
        for i in range(len(bigWord) - len(smallWord) + 1):
            for j in range(len(smallWord)):
                if bigWord[i + j] == smallWord[j]:
                    check += 1
                    if check == len(smallWord):
                        array.append(i)
                else:
                    check = 0
        return array

print("Enter the big number:")
inp1 = str(input())
print("Enter the small number:")
inp2 = str(input())
sampleWord = Words(inp1, inp2)
sampleWord.printFunc()
print("Index is:", sampleWord.calculatingLocation())

    