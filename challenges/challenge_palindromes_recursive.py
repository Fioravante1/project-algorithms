# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False
    if low_index < high_index:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
