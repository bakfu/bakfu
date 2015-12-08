# -*- coding: utf-8 -*-

import pytest

from bakfu.core import Chain
from bakfu.classify.cluster import ward_sklearn
from bakfu.data.simple import SimpleDataSource
from bakfu.process.vectorize.vec_sklearn import CountVectorizer
import bakfu.classify.ml

def test_forest():
    data=((0,'group_A'),
          (1,'group_B'),
          (2,'group_C')
          )
    test_subject = Chain().load('data.simple',data).process('vectorize.sklearn')
    test_subject.data['labels'] = [1,2,3]

    data=((0,'group_C'),
          (1,'group_B'),
          (2,'group_A')
          )
    test_subject.load("data.simple",data)

    test_subject.process('ml.forest',action='fit', n_estimators=300)
    test_subject.process('ml.forest',action='predict')

    assert test_subject.get_chain('classifier_result').tolist() == [3, 2, 1]


def test_extratrees():
    data=((0,'group_A'),
          (1,'group_B'),
          (2,'group_C')
          )
    test_subject = Chain().load('data.simple',data).process('vectorize.sklearn')
    test_subject.data['labels'] = [1,2,3]

    data=((0,'group_C'),
          (1,'group_B'),
          (2,'group_A')
          )
    test_subject.load("data.simple",data)

    test_subject.process('ml.extratrees',action='fit', n_estimators=300)
    test_subject.process('ml.extratrees',action='predict')

    assert test_subject.get_chain('classifier_result').tolist() == [3, 2, 1]
