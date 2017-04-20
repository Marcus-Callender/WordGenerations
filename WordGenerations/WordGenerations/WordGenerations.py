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

    for z in range(NumberOfWords):
        words[z].mutate();

    for z in range(NumberOfWords):
        words[z].display();

        if (z == NumberOfWords - 1):
            print('\n', end = '');
        else:
            print(', ', end = '');

    #hello = "hello";
    #print(hello[-1]);
    #
    #hello = Add(0, 'Y', hello);
    #print(hello);
    #
    #hello = Add(7, 'Y', hello);
    #print(hello);
    #
    #hello = Add(5, 'Y', hello);
    #print(hello);
    #
    #hello = remove(2, hello);
    #print(hello);     
    #
    #hello = remove(1, hello);
    #print(hello);
    #
    #hello = remove(6, hello);
    #print(hello);   
    #
    #marcus = "marcus";
    #print(marcus);
    #marcus = swap(2, 4, marcus);
    #print(marcus);

    hello = CWord();
    hello.SetWord("hello");
    
    print("comp: " + str(hello.Compare("hello")));
    print("comp: " + str(hello.Compare("yellow")));
    print("comp: " + str(hello.Compare("llohey")));
    print("comp: " + str(hello.Compare("goodbye")));

    print(hello.remove(1, hello.contents));
    print(hello.remove(0, hello.contents));
    print(hello.remove(4, hello.contents));

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

def remove(pos, string):
    string = string[:pos - 1] + string[pos:];

    return string;

def swap(pos1, pos2, string):
    
    while(pos2 == pos1):
       pos2 = random.randrange(0, len(string));

    char2 = string[pos2 - 1];
    char1 = string[pos1 - 1];

    if (pos1 > pos2):
        temp = pos1;
        pos1 = pos2;
        pos2 = temp;

    print("######");
    print("0 - " + str(pos1) + ": " + string[:pos1]);

    print(str(pos1) + " - " + str(pos2) + ": " + string[pos1 : pos2]);

    print(str(pos2) + " - end : " + string[pos2:]);
    print("######");

    string = string[: pos1 - 1] + char2 + string[pos1 : pos2 - 1] + char1 + string[pos2:];

    return string;
    


main();

