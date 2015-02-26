from bakfu.core.routes import register
from bakfu.core.classes import Processor


@register('tools.dbg')
class DebugTool(Processor):   
    '''
    Run a pdb or ipython instance at a given point.
    '''
    def run(self, baf, *args, **kwargs):
        if kwargs.get('enable',0) == 1:
            try:
                import IPython;IPython.embed()
            except:
                import pdb;pdb.set_trace()
