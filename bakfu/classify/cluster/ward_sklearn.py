# -*- coding: utf-8 -*-

'''
Ward clustering using sklearn
'''

from sklearn.cluster import AgglomerativeClustering

from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseClusterizer


@register('cluster.ward')
class WardClusterizer(BaseClusterizer):

    init_kwargs = ('n_clusters',)
    classifier_class = AgglomerativeClustering
