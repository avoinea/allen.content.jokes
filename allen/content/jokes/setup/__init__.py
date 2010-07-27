""" Setup
"""
import logging

from z3c.indexer import interfaces
from z3c.indexer.index import TextIndex
from z3c.indexer.index import FieldIndex
from z3c.indexer.index import SetIndex

from zope.intid import IntIds
from zope.intid.interfaces import IIntIds
from zope.publisher.browser import BrowserPage
from zope.component import ComponentLookupError
from zope.app.component.site import LocalSiteManager
from zope.app.component.site import SiteManagementFolder

logger = logging.getLogger('allen.content.jokes.setup')

class Setup(BrowserPage):
    """ Setup site
    """
    def __call__(self, **kwargs):
        """ Setup
        """
        site = self.context

        # Site manager
        try:
            sm = site.getSiteManager()
        except ComponentLookupError, err:
            sm = LocalSiteManager(site)
            site.setSiteManager(sm)

        # Catalog folder
        if 'catalog' not in sm:
            catalog = SiteManagementFolder()
            sm['catalog'] = catalog
            logger.info('Added catalog folder')

        # Intids utility
        if 'intids' not in sm['catalog']:
            intids = IntIds()
            sm['catalog']['intids'] = intids
            sm.registerUtility(intids, IIntIds)
            logger.info('Registered utility intids')

        # Setup text index
        if 'jokes.text' not in sm['catalog']:
            textIndex = TextIndex()
            sm['catalog']['jokes.text'] = textIndex
            sm.registerUtility(textIndex, interfaces.IIndex, name='jokes.text')
            logger.info('Registered index jokes.text')

        # Setup title index
        if 'jokes.title' not in sm['catalog']:
            titleIndex = FieldIndex()
            sm['catalog']['jokes.title'] = titleIndex
            sm.registerUtility(titleIndex, interfaces.IIndex, name='jokes.title')
            logger.info('Registered index jokes.title')

        # Setup description index
        if 'jokes.description' not in sm['catalog']:
            descriptionIndex = TextIndex()
            sm['catalog']['jokes.description'] = descriptionIndex
            sm.registerUtility(descriptionIndex, interfaces.IIndex, name='jokes.description')
            logger.info('Registered index jokes.description')

        # Setup updated index
        if 'jokes.effective' not in sm['catalog']:
            updatedIndex = FieldIndex()
            sm['catalog']['jokes.effective'] = updatedIndex
            sm.registerUtility(updatedIndex, interfaces.IIndex, name='jokes.effective')
            logger.info('Registered index jokes.effective')

        # Setup tags index
        if 'jokes.tags' not in sm['catalog']:
            tagsIndex = SetIndex()
            sm['catalog']['jokes.tags'] = tagsIndex
            sm.registerUtility(tagsIndex, interfaces.IIndex, name='jokes.tags')
            logger.info('Registered index jokes.tags')

        return 'Setup complete'
