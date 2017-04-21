from Word import CWord

import random

NumberOfWords = 12;

def main():
    generations = 1;
    wordToFind = "confidant";
    words = [None] * NumberOfWords;

    # creates the class instances
    for z in range(NumberOfWords):
        words[z] = CWord();

    DisplayWords(words, generations);
    Sort(words, wordToFind);

    #loops until the most matching word is a 100% match
    while (not CheckFoundWord(words, wordToFind)):
        CreateNewWords(words);
    
        for z in range(NumberOfWords):
            words[z].Mutate();
    
        Sort(words, wordToFind);
        generations += 1;
        DisplayWords(words, generations);

        system("cls");

def Sort(words, wordToFind):
    z = 0;
    x = 1;

    # loops over the words array, starting at the begining 
    while (z < len(words)):
        # loops over the words greater than the z value until the end each time the z value increses
        while (x < len(words)):
            # if the z word is less or as connected to the x word they swap places in the array
            if (words[z].Compare(wordToFind) <= words[x].Compare(wordToFind)):
                temp = words[z];
                words[z] = words[x];
                words[x] = temp;
            x += 1;
        z += 1;
        x = z + 1;

def CheckFoundWord(words, wordToFind):
    print(words[0].Compare(wordToFind) * 100);

    return words[0].Compare(wordToFind) == 1.0;

def DisplayWords(words, generations):
    #if (generations % 50 == 0):
    print("This is Gen " + str(generations) + ": ");
    
    for z in range(NumberOfWords):
        words[z].Display();
    
        if (z == NumberOfWords - 1):
            print('\n', end = '');
        else:
            print(', ', end = '');

def CreateNewWords(words):
    length = len(words);
    length *= 0.5;
    length = int(length);

    # an array of unasigned values the size of half the number of words
    # TODO make the size of this array scale with the number of words
    seccondHalfSet = [-1, -1, -1, -1, -1, -1];
    values = 0;

    #for z in range(length):
    #    seccondHalfSet[z] = -1;

    while (values < length):
        randomPos = random.randrange(0, length);

        if (seccondHalfSet[randomPos] == -1):
            seccondHalfSet[randomPos] = values;
            values += 1;

    for z in range(length):
        words[z + length].SetWord(words[z].GetFirstHalf() + words[seccondHalfSet[z]].GetSeccondHalf());
    

    
main();

