# -*- coding: utf-8 -*-
'''
tag_treetagger.py

This module is a wrapper to TreeTagger.

'''

import os
import string
import sklearn
from itertools import chain

from bakfu.core.routes import register
from bakfu.process.base import BaseProcessor


try:
    import pattern.fr
    import pattern.en
except:
    pass

@register('tagging.pattern')
class PatternTagger(BaseProcessor):
    '''
    Pre-processes data with pattern.

    :Example:

    >>>from bakfu.examples.dataset1 import DATA
    >>>import nltk
    >>>baf = bakfu.Chain(lang="en")
    >>>baf.load("data.simple",DATA)
    >>>baf.process('tagging.pattern')
    >>>baf.process('vectorize.sklearn',
    ...        min_df = 2,
    ...        ngram_range=(1, 3),
    ...        #stop_words=nltk.corpus.stopwords.words(baf.get('language')),
    ...        max_features=100,
    ...        tokenizer=lambda x:x,
    ...        )
    ...        preprocessor=lambda x:x,
    >>>print(baf.get_chain("vectorizer").get_feature_names())
    >>>print(baf.get_chain("vectorizer_result").toarray()[0])
    '''

 

    init_args = ()
    init_kwargs = ()
    run_args = ()
    run_kwargs = ()

    def __init__(self, *args, **kwargs):
        super(PatternTagger, self).__init__(*args, **kwargs)
        self.tagger =  pattern.fr.parsetree
        #if self.lang == 'fr':
            #self.tagger = pattern.fr.parsetree
        #elif self.lang == 'en':
            #self.tagger = pattern.en.parsetree 

    def run(self, caller, *args, **kwargs):
        '''
        TODO:CLEAN UP
        '''
        super(PatternTagger, self).run(caller, *args, **kwargs)

        data_source = caller.get_chain('data_source')
        self.caller=caller

        cur_data = data_source.get_data()
        print(cur_data)
        #import IPython;IPython.embed()

        def tag(sentence):
            lemmas = []
            [lemmas.extend(a.lemma) for a in self.tagger(sentence,tokenize = True,  tags = True, chunks = True, relations = True, lemmata = True,   light = False)]
            return lemmas

        result = [tag(s) for s in cur_data]
        caller.data['result'] = result

        #reformat data to ((id,data),...)
        #note: data now contains lists of tokens instead of sentences
        uids = data_source.get_uids()
        new_data = zip(uids, result)

        #Assign processed data to a new data source
        new_data_source = self.caller.load_unchained("data.simple", new_data)

        new_data_source.meta_data = {"tokenized":True}

        self._data.update(
            {'result':result,
             'tagger_result':result,
             'data_source':new_data_source,
            })
        return self
