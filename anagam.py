# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input("Enter your initial string \n")
anagram = input("Enter your second string \n")
word = word.replace(" ", "").lower()
anagram = anagram.replace(" ", "").lower()

def find_anagram(word, anagram):
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)
        if (sorted_word == sorted_anagram):
            return True
        else:
            return False
print(find_anagram(word, anagram))

