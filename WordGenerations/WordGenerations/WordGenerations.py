from Word import CWord

NumberOfWords = 12;

def main():
    wordToFind = "confidant";

    words = [None] * NumberOfWords;

    for z in range(NumberOfWords):
        words[z] = CWord();

    for z in range(NumberOfWords):
        words[z].display();

    print("hello");
    myNumber = NumberOfWords;
    print("my number is: " + str(myNumber));

    print(words);


main();

