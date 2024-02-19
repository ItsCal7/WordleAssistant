import linecache
greenLetters = {
}
yellowLetters = {
}
greyLetters = []
possibleWords = []
antiDuplicates = []
easyList = "answers.txt"
regularList = "valid-wordle-words.txt"

def search(fileList):
    possibleWords.clear()
    for i in range(1, 148566):
        lineBool = True
        line = linecache.getline(fileList, i)
        for letter in greenLetters:
            if not ((letter in line and line.find(letter) == greenLetters.get(letter)) or (letter in line and line.rfind(letter) == greenLetters.get(letter))):
                lineBool = False
        for letter in antiDuplicates:
            if letter in antiDuplicates and list.count > 1:
                lineBool = False
        for letter in yellowLetters:
            if letter in line and yellowLetters.get(letter) == line.find(letter):
                lineBool = False
            elif letter not in line:
                lineBool = False
        for letter in greyLetters:
            if letter in line:
                lineBool = False
        if lineBool:
            possibleWords.append(line)


def addGrey(letter):
    if letter in greenLetters or letter in yellowLetters:
        antiDuplicates.append(letter)
    else:
        greyLetters.append(letter)


def addGreen(letter, position):
    # if letter in greenLetters:
    #     greenLetters.get(letter).append(position)
    greenLetters.update({letter: position})

def inGreen(letter):
    pass


def addYellow(letter, position):
    yellowLetters.update({letter: position})


def display():
    total = 0
    for word in possibleWords:
        if not word == '':
            word = word.strip('\n')
            total += 1
            print(word)
    print("Total:", total)


if __name__ == "__main__":
    textFile = regularList
    while True:
        userInput = input("1. To add Green Letter, 2. To add a Yellow Letter, 3. To add Grey Letter, 4. To search for matching words")
        if userInput.lower() == "e":
            textFile = easyList
            print("Easy Mode Activated")
        if userInput == "1":
            greenLetter = input("Enter One Green Letter: ").lower()
            greenPos = int(input("Enter Position of Letter (0-4)"))
            addGreen(greenLetter, greenPos)
        if userInput == "2":
            yellowLetter = input("Enter One Yellow Letter: ").lower()
            yellowPos = int(input("Enter Position of Letter (0-4)"))
            addYellow(yellowLetter, yellowPos)
        if userInput == "3":
            greyLetter = input("Enter One Grey Letter: ").lower()
            addGrey(greyLetter)
        if userInput == "4":
            search(textFile)
            display()
