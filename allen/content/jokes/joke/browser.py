from zope.app import zapi
from zope.component import getMultiAdapter
from zope.formlib.form import Fields, PageEditForm
from zope.publisher.browser import BrowserPage
from allen.content.jokes.interfaces import IJoke
from zope.app.file.interfaces import IImage
from zope.app.file.interfaces import IFile

class Edit(PageEditForm):
    form_fields = Fields(IJoke)

class View(BrowserPage):
    """
    """
    def thumbnail(self, context=None, size='thumbnail'):
        if not context:
            context = self.context

        for key, doc in context.items():
            if not IImage.providedBy(doc):
                continue

            scale = getMultiAdapter((doc, self.request), name=u'scale')
            thumb = scale.publishTraverse(self.request, size)
            if thumb.getSize():
                return zapi.absoluteURL(doc, self.request)
        return ''

    @property
    def description(self):
        description = self.context.description
        cut = getattr(self, 'cuttext', 0)
        if not cut:
            return description.replace('\n', '<br />')

        description_list = description.split(' ')
        if len(description_list) <= cut + 3:
            return description
        return ' '.join(description_list[:cut]) + '...'

    def __call__(self, **kwargs):
        if self.request:
            kwargs.update(self.request.form)
        self.cuttext = kwargs.get('cuttext', 0)
        return self.index()
