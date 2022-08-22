"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 14
Homework Problem # 6
Description of Problem (1-2 sentence summary in your own words):
Create class that evaluates and manipulates English sentence, test method
"""
import string
import random

class Sentence:
    '''Create class evaluates and manipulates and English sentence'''
    def __init__(self, string_inp = ""):
        '''Initialize constructor with default string ("") argument'''
        # Remove punctuation in string.
        for char in string.punctuation:
            string_inp = string_inp.strip().replace(char," ")
        # Create list of words
        self.__string_inp = string_inp = [word for word in string_inp.split(" ") if word]

    def get_all_words (self):
        '''Method take no argument, return sentence as a list.'''
        return self.__string_inp

    def get_word (self, index):
        '''Method get desire word, return empty string if index outside of range.'''
        if index < len(self.__string_inp):
            return self.__string_inp[index]   
        else:
            return ""

    def set_word (self, index, new_word):
        '''Change word at given index, not return anything.'''
        self.__string_inp[index] = new_word

    def scramble (self):
        '''Take no argument, return scrambled list of all words.'''
        scramble_lst = random.sample(self.__string_inp, len(self.__string_inp))
        return scramble_lst

    def __repr__(self):
        '''return string with a period at the end'''
        self.sentence_s = " ".join(self.__string_inp)
        if "." not in self.sentence_s:
            self.sentence_s += "."
        return self.sentence_s

if __name__ == "__main__":
    string_in = "I' like% superman so ^much."
    sentence_1 = Sentence(string_in) # Create object
  
    # Test set_word() method.
    sentence_1.set_word(1, "hate")
    assert sentence_1.get_word(1) == "hate", "set_word() method not work."
    print("Sentence unit test successful")

    # Print results.
    print(f"Original version: {string_in}")
    print(f'Scrambled version: {" ".join(sentence_1.scramble())}')
    print(f"Final version: {repr(sentence_1)}") # Also can use print(f"Final version: {sentence_1}")
  
