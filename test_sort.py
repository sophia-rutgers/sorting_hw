from bubble import *
from quicksort import *
import numpy as np

def test_bubble_order():
    l = [1,6,4]
    assert np.all(BubbleSort([l])) == np.all([1,4,6])

def test_bubble_empty():
    l = []
    assert len(BubbleSort(l)) ==0

def test_bubble_duplicate():
    l = [1,6,4,4]
    assert np.all(BubbleSort([l])) == np.all([1,4,4,6])

def test_bubble_single_element():
    l = [1]
    assert len(BubbleSort([l])) == 1

def test_quicksort_order():
    l = [1,6,4]
    assert np.all(QS([l])) == np.all([1,4,6])

def test_quicksort_empty():
    l = []
    assert len(QS(l)) ==0

def test_quicksort_duplicate():
    l = [1,6,4,4]
    assert np.all(BubbleSort([l])) == np.all([1,4,4,6])

def test_quicksort_single_element():
    l = [1]
    assert len(QS([l])) == 1
