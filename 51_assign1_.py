#Find all close matches of input stringd from a list

from difflib import get_close_matches
word="appel"
pattern=["ape","apple","banana","papaya","aple"]

print(get_close_matches(word,pattern))