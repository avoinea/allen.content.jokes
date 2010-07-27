from zope.interface import implements
from allen.content.jokes.interfaces import IJokesPage

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Page(Content):
    """ Page content-type
    """
    implements(IJokesPage)

    title = DCProperty('title')
    description = DCProperty('description')
    servers = ()
    tags = ()
    max_items = 15
    order = 10
