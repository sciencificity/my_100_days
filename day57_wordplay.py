import sys
import day56_scrabble

# which words contain double uu's or similar?
def words_with_double(letter):
    '''
        Returns the words which contain a double of letter
    '''
    txt = letter + letter
    words = []
    for word in day56_scrabble.wordlist:
        if txt in word:
            words.append(word)
    return words

letter = input('What letter would you like to check for doubles? Please enter a letter: >> ')

print(words_with_double(letter))

# okay which words do not have any double letters?
def no_doubles():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    list_no_doubles = []
    doubles = [letter+letter for letter in letters]
    print(doubles)
    for dup_let in doubles:
        has_double = False
        for word in day56_scrabble.wordlist:
            if dup_let in word:
                has_double = True
                break
        if not has_double:
            print(f"There's no words with {dup_let}")
            list_no_doubles.append(dup_let)
    return list_no_doubles

print(no_doubles())
    
