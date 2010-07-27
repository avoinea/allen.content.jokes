import logging
from zope.intid import addIntIdSubscriber, removeIntIdSubscriber
from z3c.indexer.indexer import index as z3c_index
from z3c.indexer.indexer import unindex

logger = logging.getLogger('allen.content.jokes.catalog.events')

def joke_on_add(obj, evt):
    """ Handle add """
    try:
        addIntIdSubscriber(obj, evt)
        z3c_index(obj)
    except Exception, err:
        logger.exception(err)
    else:
        logger.debug('Successfully indexed using z3c.indexer')

def joke_on_change(obj, evt):
    """ Handle changes """
    try:
        z3c_index(obj)
    except Exception, err:
        logger.exception(err)
    else:
        logger.debug('Successfully re-indexed using z3c.indexer')

def joke_on_delete(obj, evt):
    """ Handle object delete """
    try:
        unindex(obj)
        removeIntIdSubscriber(obj, evt)
    except Exception, err:
        logger.exception(err)
    else:
        logger.debug('Successfully unindexed')
