#import Word
from Word import CWord

NumberOfWords = 12;

def main():
    words = [None] * NumberOfWords;

    for z in range(NumberOfWords):
        words[z] = CWord();

    for z in range(NumberOfWords):
        #print(words[z].contents);
        words[z].display();

    print("hello");
    myNumber = NumberOfWords;
    print("my number is: " + str(myNumber));

    print(words);


main();

