def main():
    book_Path = "books/frankenstein.txt"
    text = getText(book_Path)
    word_Count = getWords(text)
    character_Count = getChars(text)
    sorted_character_count = getSortedChars(character_Count)
    printReport(book_Path, word_Count, sorted_character_count)

# takes the previously constructed dict of characters and the number of times each occurs in the book and 1. sorts it and 2. filters it to alphabetical values only before 3. returning it
def getSortedChars(unsortedCharCount):
    sortedDict = dict(sorted(unsortedCharCount.items(), key=lambda item: item[1], reverse=True))
    alphaSortedDict = {}
    for char, count in sortedDict.items():
        if char.isalpha():
            alphaSortedDict[char] = count
    return alphaSortedDict
        
# takes the book path, the word count and the previously sorted and filterd dictionary of alphabetical values and the times they were used in the book and constructs & prints a report with the information
def printReport(book_Path, word_Count, sorted_character_count):
    print(f"--- Begin report of {book_Path} ---")
    print(f"{word_Count} words found in the document")
    print()
    for char, count in sorted_character_count.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")


# takes the text from a book and returns how often each charater was used in a book
def getChars(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars



# takes the text of a book and counts the words in it
def getWords(text):
    return len(text.split())

# takes the path to a book and gives back the text in that book
def getText(path):
    with open(path) as f:
        return f.read()


main()