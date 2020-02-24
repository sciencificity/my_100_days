"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""

import re

def has_vowel(string):
    """Return True iff the string contains one or more vowels."""
    return bool(re.search(r'[aeiou]', string))


def is_integer(string):
    """Return True iff the string represents a valid integer."""
    return bool(re.search(r'^-?[0-9]+$', string))

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""
    return bool(re.search(r'^-?[0-9]+/0?[1-9]+[0-9]*$', string))


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""
    return bool(re.search(r'^([0-9]{4})-([0][1-9]|[1][0-2])-(([0][1-9])|([1-2][0-9])|([3][0-1]))$', string))


def is_number(string):
    """Return True iff the string represents a decimal number."""
    return bool(re.search(r'^-?(\d+[.]?\d* | \.\d+)$', string, re.VERBOSE))


print(f'''In is_number: {is_number('-.5')}''')
def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
    
def is_valid_uuid(uuid):
    return bool(re.search(r'''
    ^
    [a-f\d]{8} # 8 hexdecimal digits
    -
    [a-f\d]{4} # 4 hexdecimal digits
    -
    [a-f\d]{4} # 4 hexdecimal digits
    -
    [a-f\d]{4} # 4 hexdecimal digits
    -
    [a-f\d]{12} # 12 hexdecimal digits
    $
    ''', uuid, re.IGNORECASE | re.VERBOSE))
    
    
print(is_valid_uuid('f008323-382f-ecba-83fa9-92839282193f'))

print(is_valid_uuid('f00832f3-382f-ecba-83a9-92839282193f'))

sent = 'I am flying out of ORT right now'
# Airports have 3 char names all caps - how do we write a regex to match that
print(re.search(r'[A-Z]{3}', sent))

print(re.search(r'[A-Z]{3}', 'OMGG')) # but it matches this too - how do we tell it we're looking for only 3 chars

print(re.search(r'\b[A-Z]{3}\b', 'OMGG')) # we tell it there must be a word boundary on either side

m = re.search(r'\b[A-Z]{3}\b', sent)
print(m.group())


# Looking for US zip codes in either this form:90210 or this form: 90210-4768
print(re.search(r'^\d{5}(-\d{4})?$','90210'))

print(re.search(r'^\d{5}(-\d{4})?$','90210-4563'))

print(re.search(r'\b\d{5}(-\d{4})?\b','I live in zip code 90210'))
m = re.search(r'\b(\d{5})(-\d{4})?\b','I live in zip code 90210-2345')
print(m.group()) # equivalent to saying group(0)
print(m.group(0))
print(m.group(1))
print(f'To get all groups use m.groups(): {m.groups()}. We can find length of this tuple using len {len(m.groups())}')

sentence = "I'll be flying from SAN to PDX with a stop in SFO"
matches = re.finditer(r'\b[A-Z]{3}\b', sentence) # one time use
for match in matches:
    print(match)
    
matches = re.finditer(r'\b[A-Z]{3}\b', sentence) # call again to get actual match obj
for match in matches:
    print(match.group())    
    
print(re.findall(r'\b[A-Z]{3}\b', sentence))    

print(re.findall(r'\b\d{5}\b', "90210-0438 12344"))

print(re.findall(r'\b\d{5}\b', "90210-0438-9845 12344")) # still not all that great

print(re.findall(r'\b\d{5}(-\d{4})?\b', "90210-0438-9845 12344")) # better but now we got the group not what we wanted!?!

# Findall has a catch
# If you use capturing groups it gives a tuple of all the matches including cap groups
# If we wanted the main and the optional - part we could use 2 cap grousp
print(re.findall(r'\b(\d{5})(-\d{4})?\b', "90210-0438-9845 12344"))

# But that's still a lil frustrating - if we wanted to get the match how would we do that?
print(re.findall(r'\b((\d{5})(-\d{4})?)\b', "90210-0438-9845 12344")) # we'd have to surround entire search str with ()!
# But to just the the entire match we'd have to loop over the tuple and get the first match

print([m[0] for m in re.findall(r'\b((\d{5})(-\d{4})?)\b', "90210-0438-9845 12344")])

# There is another way but it is horrid to look at
# Groups are used for capturing and also in our case to allow that substring to be matched 0 or 1 times, right
# So we tell the re that we want to find all and that the group is a non-capturing group
# After the opening ( of the cap group you put a ?: -> this turns it into a non-capturing group
# So (?: means it is a non-capturing group
print(re.findall(r'\b\d{5}(?:-\d{4})?\b', "90210-0438 12344", re.VERBOSE))

# Making that more readable
print(re.findall(r'\b \d{5} (?: -\d{4} )? \b', "90210-0438 12344", re.VERBOSE))

sentence = "This string uses ``smart'' quotes."
print(sentence)
print(sentence.replace("``",'"').replace("''", '"'))
print(re.sub(r"``|''", '"', sentence))

# re.sub is great for data normalisation
row = 'col1, col2,col3'
print(row.split(',')) # we get spaces though
print(re.findall(r'([^,]*),\s*', row)) # we have to turn off cap groups and a bit messy
print(re.split(r',', row)) # still got the space
print(re.split(r',\s*', row))

print(re.sub(r',\s*', ',', row))

# Lets say I want to convert a date in the US format mm/dd/yyyy to yyyy-mm-dd
us_format = 'from 12/22/1629 to 11/14/1643'
# I need to capture yyyy mm dd and use that in the substitution
print(re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', us_format)) # use groups in my substitution
