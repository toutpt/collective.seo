from zope import component
from zope import schema
from zope import interface
from zope.annotation.interfaces import IAttributeAnnotatable

from z3c.form import form, button

from plone.autoform.form import AutoExtensibleForm
from plone.z3cform import layout

from collective.seo import interfaces

class ISEOSettings(interface.Interface):
    """SEO settings schema"""
    
    title=schema.TextLine(title=u"Title",required=False)
    
    description=schema.TextLine(title=u"Description",required=False)
    
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
        storage = interfaces.ISEOStorage(context)
        #TODO: set values

class SEOSettingsFormWrapper(layout.FormWrapper):

    form = SEOSettingsForm

