.. _reference

=================
Processing
=================

------------------------
Treetagger 
------------------------
A Treetagger module is available.
It is set up to lemmatize data.

------------------------
Pattern
------------------------
A pattern module is available.
It is set up to lemmatize data.

To use it : :: 

    from bakfu import Chain
    baf = Chain.load(…) # load data
    baf.process('tagging.pattern')
    # by default, tagger returns tokenized data
    baf.process('vectorize.sklearn',
            tokenizer=lambda x:x,
            preprocessor=lambda x:x,
            )

_______________________
Class reference
_______________________


.. autoclass:: bakfu.process.tagging.tag_pattern.PatternTagger
   :members:
