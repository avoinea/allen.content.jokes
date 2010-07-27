from zope.interface import implements
from allen.content.jokes.interfaces import IJoke

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Joke(Content):
    """ Model
    """
    implements(IJoke)

    title = DCProperty('title')
    description = DCProperty('description')
    url = ''
    updated = None
    tags = ()
