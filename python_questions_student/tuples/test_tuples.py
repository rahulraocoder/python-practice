import pytest
from tuples import *

def test_rotate():
    assert rotate((1,2,3,4), 1) == (4,1,2,3)
    assert rotate((1,2), 3) == (2,1)
    assert rotate((), 1) == ()

def test_swap():
    assert swap((1,2), (3,4)) == ((3,4), (1,2))
    assert swap((), ()) == ((), ())

def test_tuple_distance():
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    assert abs(tuple_distance(p1, p2) - 5.0) < 0.001

def test_unpack():
    a, b, c, d = unpack((1, (2,3), 4)) 
    assert a == 1 and b == 2 and c == 3 and d == 4

def test_sort_tuples():
    assert sort_tuples([(1,3),(2,2),(1,2)]) == [(1,2),(2,2),(1,3)]
    assert sort_tuples([]) == []

def test_zip_lists():
    assert zip_lists([1,2], ['a','b']) == [(1,'a'), (2,'b')]
    assert zip_lists([], []) == []

def test_tuple_freq():
    assert tuple_freq([(1,2),(1,2),(2,3)]) == {(1,2):2, (2,3):1}
    assert tuple_freq([]) == {}

def test_transpose_matrix():
    assert transpose_matrix(((1,2),(3,4))) == ((1,3),(2,4))
    assert transpose_matrix(((),())) == ((),())

def test_concat_tuples():
    assert concat_tuples((1,2), (3,), (4,5)) == (1,2,3,4,5)
    assert concat_tuples() == ()

def test_slice_tuple():
    assert slice_tuple((0,1,2,3,4,5), 2) == (0,2,4)
    assert slice_tuple((), 2) == ()
