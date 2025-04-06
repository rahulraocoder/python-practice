import pytest
from sets import *

def test_set_union():
    assert set_union({1,2}, {2,3}) == {1,2,3}
    assert set_union(set(), {1}) == {1} 
    assert set_union() == set()

def test_set_intersection():
    assert set_intersection({1,2}, {2,3}) == {2}
    assert set_intersection({1}, {2}) == set()
    assert set_intersection() == set()

def test_set_difference():
    assert set_difference({1,2,3}, {2,3}) == {1}
    assert set_difference({1}, {2}) == {1}
    assert set_difference(set(), set()) == set()

def test_sym_diff():
    assert sym_diff({1,2}, {2,3}) == {1,3}
    assert sym_diff({1}, {1}) == set()
    assert sym_diff(set(), {1}) == {1}

def test_power_set(): 
    assert len(power_set({1,2})) == 4
    assert frozenset() in power_set({1})

def test_cartesian_product():
    assert cartesian_product({1}, {'a'}) == {(1,'a')}
    assert len(cartesian_product({1,2}, {'a','b'})) == 4

def test_set_cover():
    assert set_cover([{1,2}, {3,4}]) == {1,2,3,4}
    assert set_cover([]) == set()

def test_jaccard():
    assert jaccard({1,2}, {2,3}) == 0.5
    assert jaccard(set(), set()) == 0

def test_distinct_count():
    assert distinct_count([[1,2], [2,3]]) == 3 
    assert distinct_count([]) == 0

def test_venn_sets():
    result = venn_sets({1,2}, {2,3}, {3,4})
    assert result['A_only'] == {1}
    assert result['AB_only'] == {2}
