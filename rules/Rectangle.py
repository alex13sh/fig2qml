from . import FigmaScan
from .Item import Item

class Rectangle(Item):
    __element__ = FigmaScan.Element(name="Rectangle", type="RECTANGLE")

    def __init__(self, js):
        Item.__init__(self, js)
        
        if "cornerRadius" in js:
            self.radius = js["cornerRadius"]
        else: self.radius = 1.0
            
