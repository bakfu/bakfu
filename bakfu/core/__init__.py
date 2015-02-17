# -*- coding: utf-8 -*-
import json
import yaml

from .routes import get_processor


LANGUAGES = {
    'en':'english',
    'fr':'french',
    'de':'german',
    }

class Chain(object):
    '''
    This class can be used to manage data : loading, tagging, classifying...
    Pretty much everything you do should start here.

    :Example:

    >>> import bakfu
    >>> baf = bakfu.Chain()
    >>> baf.load("data.simple",())
    '''
    def __init__(self, *args, **kwargs):
        self.data_sources = []
        self.chain = []
        self.base_data = None
        self.data = {}

        #Defaults language to english ; set both short/long forms
        lang = kwargs.get('lang','en')
        self.data['lang'] = lang
        self.data['language'] = LANGUAGES.get(lang,'english')

    def process(self, processor_name, *args, **kwargs):
        '''Process data.'''
        processor = self.run_processor(processor_name, *args, **kwargs)
        self.chain.append(processor)
        return self

    def load(self, processor_name, *args, **kwargs):
        '''Load data.'''

        processor = self.run_processor(processor_name, *args, **kwargs)
        self.data_sources.append(processor)
        self.chain.append(processor)
        if self.base_data == None:
            self.base_data = processor
            self.data['base_data'] = processor
            self.data['main_data'] = processor
        return self

    def load_unchained(self, processor_name, *args, **kwargs):
        '''Load data.'''

        processor = self.run_processor(processor_name, *args, **kwargs)
        self.data_sources.append(processor)
        return processor

    def run_processor(self, processor_name, *args, **kwargs):
        '''
        TODO?  :
         parse args/kwargs and replace values by variables from local context :
            kwargs['this':'{self.that().this}']→ eval the term
        '''
        processor_class = get_processor(processor_name)

        try:
            previous = self.chain[-1]
        except:
            previous = self

        processor = processor_class.init_run(self, previous, *args, **kwargs)
        if not processor._prev: 
            processor._prev = previous
        previous._next = processor

        return processor

    def get(self, key):
        '''Returns an item from self.data.''' 
        return self.data[key]

    def get_chain(self, key):
        '''Looks for an item starting at the end of the chain.''' 
        return self.chain[-1].get(key)

    def last(self):
        '''return last element.'''
        return self.chain[-1]

    def __repr__(self):
       chain_str = u' -> '.join([str(elt) for elt in self.chain])
       return u'Chain : \n{chain}'.format(chain=chain_str)


    @staticmethod
    def load_json(text=None, path=None):
        '''
        Load a chain from a json description.
        Each step described in the json will be executed.

        TODO:implement
        '''
        #Load data from file
        if path is not None:
            text = open(path, "r").read()

        #parse
        json_data = json.loads(text)

        chain_data = json_data.get('chain',{})
        baf = Chain()

        for step in json_data.get("process",[]):
            step_name = step.keys()[0]
            step_data = step.get(step_name,{})
            step_args = step_data.get('args',[])

            if step_name.find('data') == 0:
                baf.load(step_name, *step_args)
            else:
                baf.process(step_name, *step_args)

        return baf

    @staticmethod
    def load_yaml(yaml=None, path=None):
        '''
        Load a chain from a yaml description.
        Each step described in the yaml will be executed.

        TODO:implement
        '''
        pass





__all__ = ['Chain',
           'get_processor',
           ]

