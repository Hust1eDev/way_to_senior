def first_unique_char(s):
    """
    This function takes a string as input and returns the first non-repeating character in the string, or None if there is no such character."""
    char_count = {}

    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1


    for char in s:
        if char_count[char] == 1:
            return char


    return None