"""
========================================
STRING METHODS DI PYTHON
========================================

Method              Description
----------------------------------------------------------
capitalize()        Converts the first character to upper case
casefold()          Converts string into lower case
center()            Returns a centered string
count()             Returns the number of times a value occurs
encode()            Returns an encoded version of the string
endswith()          Returns True if string ends with value
expandtabs()        Sets tab size
find()              Returns position of first match
format()            Formats values in a string
format_map()        Formats values using mapping
index()             Same as find(), but error if not found
isalnum()           True if alphanumeric
isalpha()           True if only alphabet
isascii()           True if ASCII characters
isdecimal()         True if decimal characters
isdigit()           True if digits
isidentifier()      True if valid identifier
islower()           True if lowercase
isnumeric()         True if numeric
isprintable()       True if printable
isspace()           True if whitespace
istitle()           True if title format
isupper()           True if uppercase
join()              Joins iterable into string
ljust()             Left justify string
lower()             Convert to lowercase
lstrip()            Remove left spaces
maketrans()         Create translation table
partition()         Split into 3 parts
replace()           Replace value
rfind()             Find last position
rindex()            Like rfind() but error if not found
rjust()             Right justify string
rpartition()        Split into 3 parts (from right)
rsplit()            Split from right
rstrip()            Remove right spaces
split()             Split string
splitlines()        Split by line breaks
startswith()        Check start of string
strip()             Trim spaces
swapcase()          Swap upper/lower
title()             Capitalize each word
translate()         Apply translation table
upper()             Convert to uppercase
zfill()             Pad with zeros
"""


#This is a comment
text = "hello world"

print(text.upper())      # HELLO WORLD
print(text.capitalize()) # Hello world
print(text.replace("world", "python")) # hello python
print(text.split())      # ['hello', 'world']
