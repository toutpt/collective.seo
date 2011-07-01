from zope import schema
from zope import interface

class ICollectiveSEOLayer(interface.Interface):
    """ A layer specific to this product. 
        Is registered using browserlayer.xml
    """

class ISEOStorage(interface.Interface):
    """SEO Storage"""

    def set(tag, value):
        """Store the tag value"""

    def get(tag):
        """Get the tag value"""

