from . import FigmaScan
from .Item import Item

class Page(Item):
    __element__ = FigmaScan.Element(name="Page", type="FRAME")

    def __init__(self, js):
        Item.__init__(self, js)
        
