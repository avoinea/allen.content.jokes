from zope.component import getMultiAdapter
from zope.formlib.form import Fields, PageEditForm
from zope.publisher.browser import BrowserPage
from allen.content.jokes.interfaces import IJokesSection, IJokesPage

class Edit(PageEditForm):
    form_fields = Fields(IJokesSection)

class View(BrowserPage):

    @property
    def content(self):
        for item in self.context.values():
            if not IJokesPage.providedBy(item):
                continue
            view = getMultiAdapter((item, self.request), name='content.html')
            return view()
        return ''

    def __call__(self, **kwargs):
        return self.index()
