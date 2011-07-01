from cgi import escape
from zope import component
from plone.app.layout.viewlets import common

from collective.seo import interfaces

from Products.CMFPlone.utils import safe_unicode

class TitleViewlet(common.TitleViewlet):
    """Override the default Plone viewlet"""

    def update(self):
        super(TitleViewlet,self).update()

        storage = interfaces.ISEOStorage(self.context)
        title = storage.get('title')

        if title:
            self.site_title = escape(safe_unicode(title))

        
