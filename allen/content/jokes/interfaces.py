from zope import schema
from allen.content.core.interfaces import IContent
from allen.content.section.interfaces import ISection

class IJokesContent(IContent):
    """ Jokes related content
    """

class IJokesSection(IJokesContent, ISection):
    """ Jokes section
    """
    title = schema.TextLine(title=u'Title', required=True)
    description = schema.Text(title=u'Description', required=False)
    order = schema.Int(title=u'Order in container', default=10)
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
    max_items = schema.Int(title=u'Max items', default=15)

class IJokesPage(IJokesContent):
    """ Collection of jokes
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    servers = schema.List(title=u'Servers', value_type=schema.TextLine(), required=False)
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
    max_items = schema.Int(title=u'Items per page', default=15)
    order = schema.Int(title=u'Order in container', default=10)

class IJokesServer(IJokesContent):
    """ Jokes categories container
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    url = schema.TextLine(title=u'URL')

class IJoke(IJokesContent):
    """ Joke object
    """
    title = schema.TextLine(title=u'Title')
    description = schema.Text(title=u'Description', required=False)
    url = schema.TextLine(title=u'URL', required=False)
    updated = schema.Datetime(title=u'Effective date')
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
