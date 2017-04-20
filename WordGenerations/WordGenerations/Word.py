import random
import math

class CWord:

    def __init__(self):
        self.contents = "";
        self.length = 0;

        self.wordMinLength = 2;
        self.wordMaxLength = 12;

        self.mutateChangePercent = 24.0;
        self.mutateAddPercent = 7.0;
        self.mutateRemovePercent = 7.0;
        self.mutateSwapPercent = 12.0;

        self.length = random.randrange(self.wordMinLength, self.wordMaxLength);

        for z in range(self.length):
            self.contents += chr(random.randrange(97, 123));

    def SetWord(self, word):
        self.contents = word;
        self.length = len(word);

    def Mutate(self):
        temp = self.contents;
        roll = random.randrange(100);

        if (roll < self.mutateChangePercent):
            self.MutateChange();
            print("Change: " + temp + " -> " + self.contents);

        elif (roll < (self.mutateChangePercent + self.mutateAddPercent)):
            self.MutateAdd();
            print("Add: " + temp + " -> " + self.contents);

        elif (roll < (self.mutateChangePercent + self.mutateAddPercent + self.mutateRemovePercent)):
            self.MutateRemove();
            print("Remove: " + temp + " -> " + self.contents);

        elif (roll < (self.mutateChangePercent + self.mutateAddPercent + self.mutateRemovePercent + self.mutateSwapPercent)):
            self.MutateSwap();
            print("Swap: " + temp + " -> " + self.contents);

    def Compare(self, wordToFind):
        tempMe = self.contents;
        tempComparitor = wordToFind;
        matchingLetters = 0;

        z = 0;
        x = 0;

        while (z < len(tempMe)):
            while (x < len(tempComparitor)):
                if (tempMe[z] == tempComparitor[x]):
                    matchingLetters += 2;
                    tempMe = self.Remove(z, tempMe);
                    tempComparitor = self.Remove(x, tempComparitor);
                    x = -1;

                x += 1;

                if (z >= len(tempMe)):
                    break;

            z += 1;
            x = 0;

        remainingLetters = len(tempComparitor) + len(tempMe);
        letterMatchPercent = (matchingLetters / (remainingLetters + matchingLetters));
        letterMatchPercent *= 0.5;

        patternMatchPercent = 0;

        if (wordToFind[0] == self.contents[0]):
            patternMatchPercent += 1;

        for z in range(len(wordToFind) - 1):
            letter1 = wordToFind[z];
            letter2 = wordToFind[z + 1];

            for x in range(len(self.contents) - 1):
                if (self.contents[x] == letter1 and self.contents[x + 1] == letter2):
                    patternMatchPercent += 1;
                    break;
            
        if (wordToFind[-1] == self.contents[-1]):
            patternMatchPercent += 1;

        patternMatchPercent = patternMatchPercent / ( 2 + (len(wordToFind) - 1));
        patternMatchPercent *= 0.5;

        return letterMatchPercent + patternMatchPercent;

    def MutateChange(self):
        # selects a random char in the string and records it
        randomIndex = random.randrange(0, self.length);
        randomChar = self.contents[randomIndex];

        # finds a random char (a-z) that isn't the same as the original
        while(self.contents[randomIndex] == randomChar):
            randomChar = chr(random.randrange(97, 123));

        self.contents = self.Change(randomIndex, randomChar, self.contents);

    def MutateAdd(self):
        # checks the length of  the current word is below the maximum
        if (self.length <= self.wordMaxLength):

            # selects a random char (a-z) and position in the string
            randomChar = chr(random.randrange(97, 123));
            randomIndex = random.randrange(0, self.length + 1);

            self.contents = self.Add(randomIndex, randomChar, self.contents);

    def MutateRemove(self):
        # checks the length of the string is not less than the minimum
        if (self.length > self.wordMinLength):

            # selects a random char to remove
            randomPos = random.randrange(0, len(self.contents));

            self.contents = self.Remove(randomPos, self.contents);

    def MutateSwap(self):
        # selects two random positions
        pos1 = random.randrange(0, len(self.contents));
        pos2 = random.randrange(0, len(self.contents));
        
        # ensures the positions are not the same
        while(pos2 == pos1):
           pos2 = random.randrange(0, len(self.contents));

        # makes the smaller number pos1
        if (pos1 > pos2):
            temp = pos1;
            pos1 = pos2;
            pos2 = temp;

        self.contents = self.Swap(pos1, pos2, self.contents);

    def Display(self):
        print(self.contents, end = '');

    def Remove(self, pos, string):
        # the letters before the char + the letters after the char
        string = string[:pos] + string[pos + 1:];

        return string;

    def Swap(self, pos1, pos2, string):
        # records the chars at the givven points
        char1 = self.contents[pos1];
        char2 = self.contents[pos2];

        # the letters before the first pos + the seccond char + the letters between pos1 & 2 + the first char + the letters after the seccond pos
        string = string[: pos1] + char2 + string[pos1 + 1 : pos2] + char1 + string[pos2 + 1:];
    
        return string;

    def Add(self, pos, letter, string):
        # the letters before the pos + the char + the letters after the pos
        string = string[:pos] + letter + string[pos:];
    
        return string;

    def Change(self, pos, letter, string):
        # the letters before the pos + the char + the letters after the pos (excluding the old char)
        string = string[:pos] + letter + string[pos + 1:];

        return string;

    def GetFirstHalf(self):
        return self.contents[:math.ceil(self.length)];

    def GetSeccondHalf(self):
        return self.contents[math.floor(self.length):];

