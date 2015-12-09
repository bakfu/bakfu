# -*- coding: utf-8 -*-

import pytest

from bakfu.core import Chain

def test_store():
    test_subject = Chain().process('store',{'a':1})
    assert test_subject.get_chain('a') == 1
    assert test_subject.chain[-1]._data == {'a':1}

    test_subject.process('store',a=2, b=3)
    assert test_subject.get_chain('a') == 2
    assert test_subject.get_chain('b') == 3

