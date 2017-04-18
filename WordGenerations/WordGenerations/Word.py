import random

class CWord:
    mutateChangePercent = 12.0;
    mutateAddPercent = 4.0;
    mutateRemovePercent = 4.0;

    def __init__(self):
        self.contents = "";
        wordMinLength = 2;
        wordMaxLength = 12;

        wordLength = random.randrange(wordMinLength, wordMaxLength);

        for z in range(wordLength):
            self.contents += chr(random.randrange(97, 123));

        pass;

    #def initialize(self):
    #    wordLength = random.randrange(wordMinLength, wordMaxLength);
    #
    #    for z in range(wordLength):
    #        contents += chr(random.randrange(97, 123));

    def mutate(self):
        roll = random.randrange(100);

        if (roll < mutateChangePercent):
            pass;
        elif (roll < (mutateChangePercent + mutateAddPercent)):
            pass;
        elif (roll < (mutateChangePercent + mutateAddPercent + mutateRemovePercent)):
            pass;

    def conection(self, wordToFind):
        pass;

    def mutateChange(self):
        pass;

    def mutateAdd(self):
        pass;

    def mutateRemove(self):
        pass;

    def display(self):
        print(self.contents);

print("Word Loaded");

