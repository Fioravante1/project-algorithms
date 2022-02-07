def find_duplicate(nums):
    list_number = list(set(nums))
    if len(nums) <= 1:
        return False

    for number in list_number:
        if type(number) == str or number < 0:
            return False
        if nums.count(number) > 1:
            return number
    return False
