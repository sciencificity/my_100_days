                      
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        list_of_words = file.readlines()
    dict_list = [word.strip() for word in list_of_words]
    return dict_list
        

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    test_list = load_words()
    print(test_list[0:3])
    # pass # run unittests to validate
                         
                              
