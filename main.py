# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from posixpath import split
from pyparsing import Word


def readfile():
    with open("story.txt") as openfile:
        read_file = openfile.read()
        return read_file

        

def countwords():
        text = readfile()
        count = {}
        for i in text.split():
          count[i] = count.get(i, 0)+1
        print(count)
countwords()
          
            



    
 


