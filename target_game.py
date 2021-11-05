import random
import copy

def generate_grid():
    """
    Generates list of letters - i.e. grid for the game.
    e.g. ['I', 'G', 'E', 'P', 'I', 'S', 'W', 'M', 'G']
    """
    lst = [chr(random.randint(97, 122)) for i in range(9)]
    return lst

def get_words(filename: str, letters: list):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(filename, mode="r", encoding="utf-8") as dictionary:
        words_dic = []
        costil = 0
        for line in dictionary: # check every line in dictionary
            line = line.strip()
            if len(line) in range(4,10) and letters[4] in line: # check whether line contains a center char and is appropriate length
                for letah in line: # check if all letters are from (list) 'letters'
                    if letah not in letters:
                        costil = 1
                        break
                if costil == 1:
                    costil = 0
                    continue
                try: # makes sure every letter in line is in generated list
                    copylist = copy.copy(letters)
                    item_index = 0
                    while item_index < len(line):
                        copylist.remove(line[item_index])
                        item_index += 1
                    words_dic.append(line.lower())
                except:
                    continue
        return words_dic
def get_user_words():
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    while True:
        user_input = input()
        if user_input:
            user_words.append(user_input)
        else:
            break
    return user_words

def get_pure_user_words(user_words: list, letters: list, words_from_dict: list):
    """
    (list, list, list) -> list
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    lst = []
    for word in user_words:
        costil = 0
        if len(word) in range(4,10) and letters[4] in word:
            for i in word:
                if i not in letters:
                    costil = 1
                    break
            if costil == 1:
                costil = 0
                continue
            try: # makes sure every letter in word is in list of letters
                    copylist = copy.copy(letters)
                    item_index = 0
                    while item_index < len(word):
                        copylist.remove(word[item_index])
                        item_index += 1
                    if word not in words_from_dict:
                        lst.append(word)
            except:
                continue
    return lst

def new(userwords, list_words, dictwords):
    print("All your words:", userwords)
    error_words = get_pure_user_words(userwords, list_words, dictwords)
    right_words = []
    missed_words = []
    for word in userwords:
            if word in dictwords:
               right_words.append(word)
    for item in dictwords:
        if item not in userwords:
            missed_words.append(item)
    print("Dictionary words:", dictwords)
    print(len(right_words), "correct guesses:", right_words)
    print(len(missed_words), "missed words:", missed_words)
    print("Your words that match rules but are not in dictionary: ", error_words) 
    with open("result.txt", mode="w", encoding="utf-8") as result:
        result.write("Dictionary words: " + ", ".join(dictwords) + "\n")
        result.write(f"{len(right_words)} correct guesses:")
        result.write(", ".join(right_words) + "\n")
        result.write(f"{len(missed_words)} missed words:")
        result.write(", ".join(missed_words) + "\n")
        result.write("Your words that match rules but are not in dictionary: ")
        result.write(", ".join(error_words))
def results():
    letters = generate_grid()
    print(letters)
    dict_list = get_words("en.txt", letters)
    words_by_user = get_user_words()
    new(userwords= words_by_user, list_words=letters, dictwords=dict_list)
