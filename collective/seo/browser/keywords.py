from plone.app.layout.viewlets import common
from collective.seo import interfaces

class MetaKeywordsViewlet(common.DublinCoreViewlet):
    """
    """
    def update(self):
        super(MetaKeywordsViewlet,self).update()
#        self.metatags
        storage = interfaces.ISEOStorage(self.context)
        keywords = storage.get('keywords')
        description = storage.get('description')
        if keywords:
            self.metatags['keywords'] = keywords
        if description:
            self.metatags['description'] = description
