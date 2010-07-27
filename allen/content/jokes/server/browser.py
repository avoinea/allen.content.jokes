from zope.formlib.form import Fields, PageEditForm
from allen.content.jokes.interfaces import IJokesServer

class Edit(PageEditForm):
    form_fields = Fields(IJokesServer)
