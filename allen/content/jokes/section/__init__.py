from zope.interface import implements
from allen.content.jokes.interfaces import IJokesSection

from zope.dublincore.property import DCProperty
from allen.content.section.model import Section

class JokeSection(Section):
    """ Model
    """
    implements(IJokesSection)

    title = DCProperty('title')
    description = DCProperty('description')
    order = 10
    tags = ()
    max_items = 15
