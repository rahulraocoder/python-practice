import pytest
from dictionaries import (
    merge_dicts, invert_dict, word_freq, nested_sum,
    flatten_dict, dict_diff, sort_by_value, remove_duplicates,
    deep_copy_dict, dict_intersection
)

def test_merge_dicts():
    assert merge_dicts({'a':1}, {'b':2}) == {'a':1, 'b':2}
    assert merge_dicts({'a':1}, {'a':2}) == {'a':2}
    assert merge_dicts({}, {'a':1}) == {'a':1}

def test_invert_dict():
    assert invert_dict({'a':1}) == {1:'a'}
    assert invert_dict({'a':1, 'b':2}) == {1:'a', 2:'b'} 
    assert invert_dict({}) == {}

def test_word_freq():
    assert word_freq('a a b') == {'a':2, 'b':1}
    assert word_freq('') == {}
    assert word_freq('hello world hello') == {'hello':2, 'world':1}

def test_nested_sum():
    assert nested_sum({'a':1, 'b':{'c':2}}) == 3
    assert nested_sum({}) == 0
    assert nested_sum({'a':1, 'b':2}) == 3

def test_flatten_dict():
    assert flatten_dict({'a':1, 'b':{'c':2}}) == {'a':1, 'b.c':2}
    assert flatten_dict({}) == {}
    assert flatten_dict({'a':1}) == {'a':1}

def test_dict_diff():
    assert dict_diff({'a':1}, {'a':2}) == {'a':[1,2]}
    assert dict_diff({'a':1}, {'a':1}) == {}
    assert dict_diff({'a':1}, {'b':1}) == {'a':[1, None], 'b':[None, 1]}

def test_sort_by_value():
    assert sort_by_value({'a':2, 'b':1}) == {'b':1, 'a':2}
    assert sort_by_value({'a':1}) == {'a':1}
    assert sort_by_value({'a':1, 'b':1}) == {'a':1, 'b':1}

def test_remove_duplicates():
    assert remove_duplicates({'a':1, 'b':1}) == {'a':1}
    assert remove_duplicates({'a':1}) == {'a':1}
    assert remove_duplicates({'a':1, 'b':2}) == {'a':1, 'b':2}

def test_deep_copy_dict():
    d = {'a':[1]}
    copy = deep_copy_dict(d)
    d['a'].append(2)
    assert copy == {'a':[1]}
    assert deep_copy_dict({}) == {}

def test_dict_intersection():
    assert dict_intersection({'a':1}, {'a':2}) == {'a':1}
    assert dict_intersection({'a':1}, {'b':2}) == {}
    assert dict_intersection({'a':1, 'b':2}, {'a':3}) == {'a':1}
