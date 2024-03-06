#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
      self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        sentence_end_punctuation = ['.', '!', '?']
        sentence_count = sum(1 for i, char in enumerate(self.value) if char in sentence_end_punctuation and (i == len(self.value) - 1 or self.value[i+1] not in sentence_end_punctuation))
        return sentence_count