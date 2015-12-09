from bakfu.core.routes import register
from bakfu.core.classes import Processor

@register('store')
class Store(Processor):
    '''
    Store data in the chain.
    Usage :
        >>> baf.process('store',foo='bar',n=2)
        >>> baf.process('store',{'foo':'bar','n':2})
        >>> baf.get_chain('foo')
    '''
    def run(self, caller, *args, **kwargs):
        for d in args:
            self.update(**d)
        self.update(
            **kwargs
            )
        return self

