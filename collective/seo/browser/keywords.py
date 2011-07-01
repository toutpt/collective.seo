from plone.app.layout.viewlets import common
from collective.seo import interfaces

class MetaKeywordsViewlet(common.DublinCoreViewlet):
    """
    """
    def update(self):
        super(MetaKeywordsViewlet,self).update()

        storage = interfaces.ISEOStorage(self.context)
        keywords = storage.get('keywords')
        description = storage.get('description')

        if keywords:
            #first we need to remove keywords if exists
            for index, (key, value) in enumerate(self.metatags):
                if key == 'keywords':
                    self.metatags.pop(index)
            self.metatags.append(('keywords', keywords))

        if description:
            for index, (key, value) in enumerate(self.metatags):
                if key == 'description':
                    self.metatags.pop(index)
            self.metatags.append(('description', description))
