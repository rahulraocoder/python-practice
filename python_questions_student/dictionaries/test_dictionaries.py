import pytest
from dictionaries import *

def test_invert_dict():
    assert invert_dict({'a':1, 'b':2, 'c':1}) == {1:['a','c'], 2:['b']}
    assert invert_dict({}) == {}

def test_merge_dicts():
    assert merge_dicts({'a':1}, {'b':2}) == {'a':1, 'b':2}
    assert merge_dicts({'a':1}, {'a':2}) == {'a':3}
    assert merge_dicts({}, {}) == {}

def test_filter_dict():
    assert filter_dict({'a':1, 'b':2}, lambda k,v: v>1) == {'b':2}
    assert filter_dict({'a':1}, lambda k,v: True) == {'a':1}

def test_map_values():
    assert map_values({'a':1, 'b':2}, lambda x: x*2) == {'a':2, 'b':4}
    assert map_values({}, lambda x: x) == {}

def test_nested_get():
    assert nested_get({'a':{'b':1}}, ['a','b']) == 1
    assert nested_get({}, ['a']) is None

def test_swap_keys():
    assert swap_keys({'a':1}, {1:'x'}) == {1:'a', 'x':1}
    assert swap_keys({}, {}) == {}

def test_dict_diff():
    assert dict_diff({'a':1}, {'a':2}) == {'a':1}
    assert dict_diff({}, {}) == {}

def test_sort_by_value():
    assert sort_by_value({'a':3, 'b':1}) == {'b':1, 'a':3}
    assert sort_by_value({}) == {}

def test_histogram():
    assert histogram([{'a':1}, {'a':1}]) == {1:2}
    assert histogram([]) == {}

def test_with_defaults():
    assert with_defaults({'a':1}, ['a','b'], 0) == {'a':1, 'b':0}
    assert with_defaults({}, [], 0) == {}
