from persistent.dict import PersistentDict
from zope import component
from zope import interface
from zope import schema

from zope.annotation.interfaces import IAnnotations, IAttributeAnnotatable

from collective.seo import interfaces

STORAGE_KEY = "collective.seo"

class ZopeAnnotation(object):
    """Mutator based on annotation"""
    component.adapts(IAttributeAnnotatable)
    interface.implements(interfaces.ISEOStorage)

    def __init__(self, context):
        self.context = context
        self.annotation = None
    
    def get(self, tag, default=None):
        annotation = self.getAnnotation()
        if STORAGE_KEY not in annotation.keys():
            return default
        
        storage = annotation[STORAGE_KEY]
        value = storage.get(tag, None)
        return value

    def getAnnotation(self):
        """Return the persistent dict that will embed the configuration"""
        if self.annotation is None:
            self.annotation = IAnnotations(self.context)
        return self.annotation

    def set(self, tag, value):
        annotation = self.getAnnotation()
        defaults = self.get_defaults()

        if STORAGE_KEY not in annotation:
            annotation[STORAGE_KEY] = PersistentDict()
        
        annotation[STORAGE_KEY][tag] = value
