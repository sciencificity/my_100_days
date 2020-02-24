"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension3(filename):
    """Return the file extension for a full file path."""
    return(re.findall(r'^(?: \w+ [.]{1})? \w+[.]{1} (\w+)$', filename, re.VERBOSE))
    
def get_extension2(filename):
    """Return the file extension for a full file path."""
    return(re.findall(r'\.(\w+)$', filename, re.VERBOSE))    
    
def get_extension(filename):
    """Return the file extension for a full file path."""
    return(re.search(r'\.([^.]+)$', filename, re.VERBOSE).group(1))        

# >>> get_extension('archive.zip')
# 'zip'
# >>> get_extension('image.jpeg')
# 'jpeg'
# >>> get_extension('index.xhtml')
# 'xhtml'
# >>> get_extension('archive.tar.gz')
# 'gz'

print(re.findall(r'\w+[.]{1}', 'archive.zip'))
print(get_extension('archive.zip'))
print(get_extension('image.jpeg'))
print(get_extension('index.xhtml'))
print(get_extension('archive.tar.gz'))
print(get_extension2('archive.zip'))
print(get_extension2('image.jpeg'))
print(get_extension2('index.xhtml'))
print(get_extension2('archive.tar.gz'))

print(get_extension3('archive.zip'))
print(get_extension3('image.jpeg'))
print(get_extension3('index.xhtml'))
print(get_extension3('archive.tar.gz'))

print('archive.tar.gz'.split('.')[-1])
print(re.split('\.', 'archive.tar.gz'))
print(re.findall(r'\b[0-2]\d:[0-5]\d\b', '10:23 43:32 67:908 24:59 23:60 23:59 00:59')) # 24:59 still matching but invalid

print(re.findall(r'\b (?:[01]\d | 2[0-3]) : [0-5]\d \b', '10:23 43:32 67:908 24:59 23:60 23:59 00:59 18:59 10:45', re.VERBOSE)) # 24:59 still matching but invalid

row = 'col1, col2,col3'
print(row.split(',')) # we get spaces though
print(re.findall(r'([^,]*),\s*', row)) # we have to turn off cap groups and a bit messy
print(re.split(r',', row)) # still got the space
print(re.split(r',\s*', row))

# write a reg exp once and use it many times through program
time_comp = re.compile(r'\b (?:[01]\d | 2[0-3]) : [0-5]\d \b', re.VERBOSE)
print(time_comp.search("00:59"))
print(time_comp.split("00:59")) # doesn't make sense here but just to show we can do
print(time_comp.findall("10:23 43:32 67:908 24:59 23:60 23:59 00:59 18:59 10:45"))

def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    pass

def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    pass

def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    pass

def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """
    pass

def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""
    pass

def abbreviate(phrase):
    """Return an acronym for the given phrase."""
    # Look for word boundary - looking for a letter that has a non-word before it
    # JavaScript however won't work for the JSON abbr.
    # Probably need a pipe to say looking for a word boundary then letter OR lowercase followed by Capital letter


def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""
    matches = re.finditer(r'\b(\w)(\w)\w\2\1\b', dictionary)
    return [m.group() for m in matches]

print(palindrome5())

def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """
    pass

def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
    pass    
