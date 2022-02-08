# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
def is_palindrome_iterative(word):
    if not word:
        return False
    else:
        return word == word[::-1]
