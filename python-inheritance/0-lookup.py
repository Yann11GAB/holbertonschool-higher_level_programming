#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object
    
    Returns:
        list: A sorted list of attributes and methods of the object
    """
    return sorted(dir(obj))
