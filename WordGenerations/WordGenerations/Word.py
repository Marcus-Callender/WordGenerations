import random

class CWord:
    mutateChangePercent = 12.0;
    mutateAddPercent = 3.0;
    mutateRemovePercent = 3.0;
    mutateSwapPercent = 3.0;

    def __init__(self):
        self.contents = "";
        self.length = 0;

        wordMinLength = 2;
        wordMaxLength = 12;

        self.length = random.randrange(wordMinLength, wordMaxLength);

        for z in range(self.length):
            self.contents += chr(random.randrange(97, 123));

    def mutate(self):
        roll = random.randrange(100);

        if (roll < mutateChangePercent):
            mutateChange();
            pass;
        elif (roll < (mutateChangePercent + mutateAddPercent)):
            pass;
        elif (roll < (mutateChangePercent + mutateAddPercent + mutateRemovePercent)):
            pass;
        elif (roll < (mutateChangePercent + mutateAddPercent + mutateRemovePercent + mutateSwapPercent)):
            pass;

    def conection(self, wordToFind):
        pass;

    def mutateChange(self):
        mutatedIndex = random.randrange(0, self.length);
        mutatedChar = self.contents[mutatedIndex];

        while(self.contents[mutatedIndex] == mutatedChar):
            mutatedChar = chr(random.randrange(97, 123));

        self.contents[mutatedIndex] = mutatedChar;

        pass;

    def mutateAdd(self):
        pass;

    def mutateRemove(self):
        pass;

    def mutateSwap(self):
        pass;

    def display(self):
        print(self.contents);

print("Word Loaded");

