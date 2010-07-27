from zope.interface import implements
from allen.content.jokes.interfaces import IJokesServer

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Server(Content):
    """ Model
    """
    implements(IJokesServer)

    title = DCProperty('title')
    description = DCProperty('description')
    url = ''
