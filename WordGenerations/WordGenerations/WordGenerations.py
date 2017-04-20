from Word import CWord

import random

NumberOfWords = 12;

def main():
    wordToFind = "confidant";

    words = [None] * NumberOfWords;

    for z in range(NumberOfWords):
        words[z] = CWord();

    for z in range(NumberOfWords):
        words[z].Display();

        if (z == NumberOfWords - 1):
            print('\n', end = '');
        else:
            print(', ', end = '');

    for z in range(NumberOfWords):
        words[z].Mutate();

    for z in range(NumberOfWords):
        words[z].Display();

        if (z == NumberOfWords - 1):
            print('\n', end = '');
        else:
            print(', ', end = '');

    testNums = [1, 4, 20, 5, 100, 4, 1];

    z = 0;
    x = 1;

    while (z < len(testNums)):
        while (x < len(testNums)):
            if (testNums[z] > testNums[x]):
                temp = testNums[z];
                testNums[z] = testNums[x];
                testNums[x] = temp;
            x += 1;
        z += 1;
        x = z + 1;

    print(testNums);
    
main();

