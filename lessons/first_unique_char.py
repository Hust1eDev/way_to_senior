def first_unique_char(s):
    """
    This function takes a string s as input and returns the index of the first non-repeating character in it.
    If there is no such character, it returns -1.

    :param s: str - The input string
    :return: int - The index of the first unique character or -1 if none exists
    """
    char_count = {}

    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1


    for char in s:
        if char_count[char] == 1:
            return char


    return None