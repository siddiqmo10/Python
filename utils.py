def find_max(lists):
    max = lists[0]
    for number in lists:
        if number > max:
            max = number
    return max

