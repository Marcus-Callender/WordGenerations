from Word import CWord

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


main();

