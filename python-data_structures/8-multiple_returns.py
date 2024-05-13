#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    Args:
        sentence (str): The string from which to extract
        the length and first character.
    Returns:
        tuple: A tuple containing the length
        of the string and its first character,
        or None if the string is empty.
    """
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
