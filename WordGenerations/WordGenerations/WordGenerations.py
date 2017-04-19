from Word import CWord

import random

NumberOfWords = 12;

def main():
    wordToFind = "confidant";

    words = [None] * NumberOfWords;

    for z in range(NumberOfWords):
        words[z] = CWord();

    for z in range(NumberOfWords):
        words[z].display();

        if (z == NumberOfWords - 1):
            print('\n', end = '');
        else:
            print(', ', end = '');

    hello = "hello";

    hello = Add(0, 'Y', hello);
    print(hello);

    hello = Add(7, 'Y', hello);
    print(hello);

    hello = Add(5, 'Y', hello);
    print(hello);
            
def Add(pos, letter, string):
    randomLetter = chr(random.randrange(97, 123));
    posInString = random.randrange(0, len(string));
    
    string = string[:pos] + letter + string[pos:];

    #if (pos == len(string) + 1):
    #    string += letter;
    #
    #elif (pos == 0):
    #    string = letter + string;
    #
    #else:
    #    string = string[:pos] + letter + string[pos:];
    #    pass;

    return string;
    pass;
    


main();

