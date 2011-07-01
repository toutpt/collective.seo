from zope import component
from zope import schema
from zope import interface
from zope.annotation.interfaces import IAttributeAnnotatable

from z3c.form import form, button

from plone.autoform.form import AutoExtensibleForm
from plone.z3cform import layout

from collective.seo import interfaces
from Products.statusmessages.interfaces import IStatusMessage

class ISEOSettings(interface.Interface):
    """SEO settings schema"""

    title=schema.TextLine(title=u"Title",required=False)

    description=schema.Text(title=u"Description",required=False)

    keywords=schema.TextLine(title=u"Keywords",required=False)

class SEOSettingsAdapter(object):

    interface.implements(ISEOSettings)
    component.adapts(IAttributeAnnotatable)

    def __init__(self, context):
        self.context = context
        self.title = u""
        self.description = u""
        self.keywords = u""
        storage = interfaces.ISEOStorage(context)
        if storage:
            self.title = storage.get('title',u"")
            self.description = storage.get('description',u"")
            self.keywords = storage.get('keywords',u"")

class SEOSettingsForm(AutoExtensibleForm, form.Form):
    
    schema=ISEOSettings

    @button.buttonAndHandler(u'Save')
    def handleSave(self, action):
        data, errors = self.extractData()
        storage = interfaces.ISEOStorage(self.context)
        storage.setAll(data)
        self.status = u"Changed saved."
        IStatusMessage(self.request).add(self.status, 'info')

        state = component.queryMultiAdapter((self.context, self.request),
                                            name='plone_context_state')
        url = state.view_url()
        self.request.response.redirect(url)
        return u""

#    def getContent(self):
#        storage = interfaces.ISEOStorage(self.context)
#        return storage.getAll()

class SEOSettingsFormWrapper(layout.FormWrapper):

    form = SEOSettingsForm

