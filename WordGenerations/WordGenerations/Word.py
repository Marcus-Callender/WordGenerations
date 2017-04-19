import random

class CWord:

    def __init__(self):
        self.contents = "";
        self.length = 0;

        self.wordMinLength = 2;
        self.wordMaxLength = 12;

        self.mutateChangePercent = 12.0;
        self.mutateAddPercent = 3.0;
        self.mutateRemovePercent = 3.0;
        self.mutateSwapPercent = 3.0;

        self.length = random.randrange(self.wordMinLength, self.wordMaxLength);

        for z in range(self.length):
            self.contents += chr(random.randrange(97, 123));

    def mutate(self):
        temp = self.contents;
        roll = random.randrange(100);

        if (roll < self.mutateChangePercent):
            self.mutateChange();
            print("Change: " + temp + " -> " + self.contents);

        elif (roll < (self.mutateChangePercent + self.mutateAddPercent)):
            self.mutateAdd();
            print("Add: " + temp + " -> " + self.contents);

        elif (roll < (self.mutateChangePercent + self.mutateAddPercent + self.mutateRemovePercent)):
            self.mutateRemove();
            print("Remove: " + temp + " -> " + self.contents);

        elif (roll < (self.mutateChangePercent + self.mutateAddPercent + self.mutateRemovePercent + self.mutateSwapPercent)):
            self.mutateSwap();
            #print("Swap: " + temp + " -> " + self.contents);

    def conection(self, wordToFind):
        pass;

    def mutateChange(self):
        mutatedIndex = random.randrange(0, self.length);
        mutatedChar = self.contents[mutatedIndex];

        while(self.contents[mutatedIndex] == mutatedChar):
            mutatedChar = chr(random.randrange(97, 123));

        #self.contents[mutatedIndex] = mutatedChar;
        self.contents = self.contents[:mutatedIndex - 1] + mutatedChar + self.contents[mutatedIndex:];

    def mutateAdd(self):
        if (self.length < self.wordMaxLength):
            randomLetter = chr(random.randrange(97, 123));
            posInString = random.randrange(0, self.length + 1);
            self.contents = self.contents[:posInString] + randomLetter + self.contents[posInString:];

    def mutateRemove(self):
        if (self.length > self.wordMinLength):
            randomPos = random.randrange(1, len(self.contents));
            self.contents = self.contents[:randomPos - 1] + self.contents[randomPos:];

    def mutateSwap(self):
        pass;

    def display(self):
        print(self.contents, end = '');

#print("Word Loaded");

