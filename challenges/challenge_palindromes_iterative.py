def is_palindrome_iterative(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return True
