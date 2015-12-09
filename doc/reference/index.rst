.. _reference

=================
Data
=================

------------------------
Simple loader
------------------------

To load and access some data: 
::
    from bakfu import Chain
    baf = Chain.load(data) # load data

The data variable must be in the following format : 
::
    [(id0,data0),(id1,data1),...]
Where id* are *integers* and data* are *str*.

------------------------
Save/load a chain
------------------------

To save a chain to a pickle file : 
::
    baf.process('pickle.save','file.pkl')

And to load it : 
::
    baf = Chain().load('pickle.load','file.pkl')


=================
Processing
=================

------------------------
Treetagger 
------------------------
A Treetagger module is available.
It is set up to lemmatize data.


To use it : 
::
    from bakfu import Chain
    baf = Chain.load(data) # load data
    baf.process('tagging.treetagger')
    # by default, tagger returns tokenized data
    baf.process('vectorize.sklearn',
            tokenizer=lambda x:x,
            preprocessor=lambda x:x,
            )


.. warning::
    The treetagger install must be accessible.


------------------------
Pattern
------------------------
A `pattern`_ module is available.
It is set up to lemmatize data.

To use it : 
::
    from bakfu import Chain
    baf = Chain.load(data) # load data
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


   
=================
Classifying
=================
.. automodule:: bakfu.classify.ml.forest
   :no-undoc-members:
   :members:
   :no-private-members:
   :no-special-members:
   :no-inherited-members:
   :show-inheritance:

=================
Tools
=================

.. automodule:: bakfu.tools.debug
   :no-undoc-members:
   :members:
   :no-private-members:
   :no-special-members:
   :no-inherited-members:
   :show-inheritance:


.. automodule:: bakfu.tools.store
   :no-undoc-members:
   :members:
   :no-private-members:
   :no-special-members:
   :no-inherited-members:
   :show-inheritance:

.. _`pattern`: https://github.com/clips/pattern
