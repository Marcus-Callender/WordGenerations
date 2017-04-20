from Word import CWord

import random

NumberOfWords = 12;

def main():
    generations = 1;
    wordToFind = "confidant";
    words = [None] * NumberOfWords;

    for z in range(NumberOfWords):
        words[z] = CWord();

    DisplayWords(words, generations);
    Sort(words, wordToFind);

    while (not CheckFoundWord(words, wordToFind)):
        CreateNewWords(words);

        for z in range(NumberOfWords):
            words[z].Mutate();

        Sort(words, wordToFind);
        generations += 1;
        DisplayWords(words, generations);

def Sort(words, wordToFind):
    z = 0;
    x = 1;

    while (z < len(words)):
        while (x < len(words)):
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

    seccondHalfSet = [-1, -1, -1, -1, -1, -1];
    count = 0;

    for z in range(length):
        seccondHalfSet[z] = -1;

    while (count < length):
        randomPos = random.randrange(0, length);

        if (seccondHalfSet[randomPos] == -1):
            seccondHalfSet[randomPos] = z;
            count += 1;

    for z in range(length):
        words[z + length].SetWord(words[z].GetFirstHalf() + words[seccondHalfSet[z]].GetSeccondHalf());
    

    
main();

