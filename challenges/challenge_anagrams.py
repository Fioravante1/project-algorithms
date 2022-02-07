def sort(word):
    unsorted_list = list(word)
    list_sorted = []

    while unsorted_list:
        small = min(unsorted_list)
        list_sorted.append(small)
        unsorted_list.pop(unsorted_list.index(small))

    return "".join(list_sorted)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return sort(first_string) == sort(second_string)
