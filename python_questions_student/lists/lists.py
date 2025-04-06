def rotate(lst: list, n: int) -> list:
    """Rotate list elements by N positions.

    Problem: Given a list and integer N, rotate elements N positions
    to the right (positive N) or left (negative N). Maintains order
    of elements during rotation.
    
    Args:
        lst: Input list to rotate
        n: Positions to rotate (positive = right, negative = left)
        
    Returns:
        New rotated list
        
    Examples:
        >>> rotate([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate([1, 2, 3], -1)
        [2, 3, 1]
        
    Edge Cases:
        - Empty list returns empty list
        - Rotation greater than length wraps around
        - Single element list returns same
    """
    pass

def chunk(lst: list, size: int) -> list[list]:
    """Split list into sublists of specified size.

    Problem: Divide a list into smaller sublists where 
    each sublist has maximum specified size.
    
    Args:
        lst: List to be chunked  
        size: Maximum size of each chunk
        
    Returns:
        List of chunks (sublists)
        
    Examples:
        >>> chunk([1,2,3,4,5], 2)
        [[1,2], [3,4], [5]]
        >>> chunk([1,2,3], 1)
        [[1], [2], [3]]
    
    Edge Cases:
        - Empty list returns empty list
        - Size larger than list returns single chunk
        - Zero size raises ValueError
    """
    pass

def flatten(nested: list) -> list:
    """Flatten an arbitrarily nested list.

    Problem: Convert a nested list structure into a flat list
    while preserving element order. Handles multiple nesting levels.
    
    Args:
        nested: List that may contain other lists recursively
        
    Returns:
        Single-level list with all elements
        
    Examples:
        >>> flatten([[1, [2]], 3])
        [1, 2, 3]
        >>> flatten([[[1]], [2]])
        [1, 2]
        
    Edge Cases: 
        - Empty list returns empty list
        - Non-list elements remain unchanged
        - Deep nesting handled recursively
    """
    pass

def dedupe(lst: list) -> list:
    """Remove duplicates while preserving order.

    Problem: Create new list with first occurrence of each element
    from original list, maintaining original order.
    
    Args:
        lst: Input list potentially containing duplicates
        
    Returns:
        New list with duplicates removed
        
    Examples:
        >>> dedupe([1, 3, 2, 3, 1])
        [1, 3, 2]
        >>> dedupe(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
        
    Edge Cases:
        - Empty list returns empty list
        - All unique elements returns same list
        - Preserves order of first occurrences
    """
    pass

def freq_count(lst: list) -> dict:
    """Count frequency of each unique element.

    Problem: Create dictionary mapping each unique element
    to its count of occurrences in the list.
    
    Args:
        lst: Input list to analyze
        
    Returns:
        Dictionary of {element: count} pairs
        
    Examples:
        >>> freq_count([1, 2, 1, 3])
        {1: 2, 2: 1, 3: 1}
        >>> freq_count(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
        
    Edge Cases:
        - Empty list returns empty dict
        - All unique elements return counts of 1
        - Handles unhashable types gracefully
    """
    pass

def transpose(matrix: list[list]) -> list[list]:
    """Transpose a 2D matrix (swap rows and columns).

    Problem: Convert matrix rows to columns and vice versa
    using nested list comprehensions.
    
    Args:
        matrix: 2D list to transpose (list of lists)
        
    Returns:
        New transposed matrix
        
    Examples:
        >>> transpose([[1, 2], [3, 4]])
        [[1, 3], [2, 4]]
        >>> transpose([[1, 2, 3]])
        [[1], [2], [3]]
        
    Edge Cases:
        - Empty matrix returns empty matrix
        - Non-rectangular matrix raises ValueError
        - Single row becomes multiple columns
    """
    pass

def running_avg(lst: list[float]) -> list[float]:
    """Calculate running averages of a sequence.

    Problem: Compute cumulative averages at each point
    in the input sequence.
    
    Args:
        lst: List of numbers to average
        
    Returns:
        List of running averages
        
    Examples:
        >>> running_avg([1, 2, 3, 4])
        [1, 1.5, 2, 2.5]
        >>> running_avg([10, 10, 10])
        [10, 10, 10]
        
    Edge Cases:
        - Empty list returns empty list
        - Single element returns that element
        - Preserves float precision
    """
    pass

def zigzag(lst: list) -> list:
    """Reorder elements in zig-zag pattern (a < b > c < d > e).

    Problem: Rearrange elements so they alternate between
    smaller-than-next and greater-than-next.
    
    Args:
        lst: List of comparable elements
        
    Returns:
        New list in zig-zag order
        
    Examples:
        >>> zigzag([4, 3, 7, 8, 6, 2])
        [3, 7, 4, 8, 2, 6]
        >>> zigzag([1, 4, 3, 2])
        [1, 4, 2, 3]
        
    Edge Cases:
        - Empty list returns empty list
        - Single element returns same list
        - Already zigzag returns same list
    """
    pass

def partition(lst: list, condition: callable) -> tuple[list, list]:
    """Split list into elements matching condition and others.

    Problem: Divide list into two sublists - one with elements
    that satisfy the condition, and one with remaining elements.
    
    Args:
        lst: List to partition
        condition: Function that returns True for matching elements
        
    Returns:
        Tuple of (matching_elements, non_matching_elements)
        
    Examples:
        >>> partition(range(10), lambda x: x%2==0)
        ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
        >>> partition(['a', 'b', 'c'], lambda x: x in 'aeiou')
        (['a'], ['b', 'c'])
        
    Edge Cases:
        - Empty list returns two empty lists
        - All match returns (full_list, [])
        - None match returns ([], full_list)
    """
    pass

def windows(lst: list, size: int) -> list[tuple]:
    """Generate sliding windows of elements.

    Problem: Create overlapping subsequences of elements
    with specified window size.
    
    Args:
        lst: List to create windows from
        size: Number of elements in each window
        
    Returns:
        List of tuples representing each window
        
    Examples:
        >>> windows([1, 2, 3, 4], 2)
        [(1, 2), (2, 3), (3, 4)]
        >>> windows(['a', 'b', 'c'], 3)
        [('a', 'b', 'c')]
        
    Edge Cases:
        - Empty list returns empty list
        - Size larger than list returns empty list
        - Size 1 returns each element individually
    """
    pass


if __name__ == "__main__":
    assert rotate([1,2,3,4,5], 2) == [3,4,5,1,2]
    print("All test cases pass")
