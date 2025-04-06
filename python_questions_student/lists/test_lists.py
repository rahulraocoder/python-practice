import pytest
from lists import rotate, chunk, flatten, dedupe, freq_count, transpose, running_avg, zigzag, partition, windows

def test_rotate():
    assert rotate([1,2,3,4,5], 2) == [3,4,5,1,2]
    assert rotate([1,2,3,4,5], -1) == [5,1,2,3,4] 
    assert rotate([1,2,3], 5) == [3,1,2]
    assert rotate([], 2) == []

def test_chunk():
    assert chunk([1,2,3,4,5,6], 2) == [[1,2], [3,4], [5,6]]
    assert chunk([1,2,3,4,5], 3) == [[1,2,3], [4,5]]
    assert chunk([], 2) == []

def test_flatten():
    assert flatten([[1,2], [3,4], [5]]) == [1,2,3,4,5]
    assert flatten([[], [1], [2,3]]) == [1,2,3]
    assert flatten([[[]]]) == []

def test_dedupe(): 
    assert dedupe([1,3,2,3,1]) == [1,3,2]
    assert dedupe(['a','b','a','c']) == ['a','b','c']
    assert dedupe([]) == []
