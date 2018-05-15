# -*- coding: utf-8 -*-

'''
HDBSCAN clustering

https://github.com/lmcinnes/hdbscan
'''
import hdbscan
from  hdbscan import HDBSCAN
from hdbscan import RobustSingleLinkage

from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseClusterizer


@register('cluster.hdbscan')
class HDBSCANClusterizer(BaseClusterizer):
    '''
    baf.process('cluster.hdbscan', min_cluster_size=2)
    hdbscan(X, min_cluster_size, min_samples, alpha, metric, p, leaf_size,
    algorithm, memory, approx_min_span_tree, gen_min_span_tree,
    core_dist_n_jobs)

    '''

    init_kwargs = ('min_cluster_size', 'min_samples', 'alpha', 'metric', 'p', 'leaf_size',
        'algorithm', 'memory', 'approx_min_span_tree', 'gen_min_span_tree',
        'core_dist_n_jobs' )
    classifier_class = HDBSCAN


@register('cluster.hdbscan-rsl')
class HDBSCANClusterizer(BaseClusterizer):
    """Robust single linkage clustering"""
    init_kwargs = ('cut', 'k', 'alpha', 'gamma', 'metric', 'algorithm' )
    classifier_class = RobustSingleLinkage
