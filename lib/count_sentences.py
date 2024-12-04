#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use the property setter to validate

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        cleaned_value = re.sub(r"[!?]+", ".", self.value)  # Replace ? and ! with .
        sentences = [s.strip() for s in cleaned_value.split(".") if s.strip()]
        return len(sentences)
