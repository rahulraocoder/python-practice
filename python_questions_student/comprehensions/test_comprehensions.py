import pytest
from comprehensions import *

def test_flatten_matrix():
    assert flatten_matrix([[1,2], [3,4]]) == [1,2,3,4]
    assert flatten_matrix([[]]) == []

def test_create_dict():
    assert create_dict(['a','b','c'], [1,2,3], lambda k,v: v>1) == {'b':2, 'c':3}
    assert create_dict([], [], lambda k,v: True) == {}

def test_unique_words():
    assert unique_words("hello world", "world peace") == {'hello','world','peace'}
    assert unique_words("") == set()

def test_even_combos():
    assert set(even_combos([1,2,3], [4,5,6])) == {(1,5), (2,4), (2,6), (3,5)}
    assert even_combos([], []) == []

def test_transform_dict():
    assert transform_dict({'a':1, 'b':2}, lambda x: x*x) == {'a':1, 'b':4}
    assert transform_dict({}, lambda x: x) == {}

def test_tuples_to_dict():
    assert tuples_to_dict([(1,'a'),(2,'b'),(1,'c')]) == {1:{'a','c'}, 2:{'b'}}
    assert tuples_to_dict([]) == {}

def test_filter_transform():
    assert filter_transform([1,2,3,4], lambda x: x>2, lambda x: x*x) == [9,16]
    assert filter_transform([], lambda x: True, lambda x: x) == []

def test_reformat_data():
    assert reformat_data([{'a':1}, {'a':2, 'b':3}]) == {'a':[1,2], 'b':[3]}
    assert reformat_data([]) == {}

def test_nested_combos():
    assert set(nested_combos([[1,2], ['a','b']])) == {(1,'a'),(1,'b'),(2,'a'),(2,'b')}
    assert nested_combos([]) == []

def test_char_counts():
    assert char_counts("hello") == {'h':1, 'e':1, 'l':2, 'o':1}
    assert char_counts("") == {}
