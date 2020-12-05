from . import FigmaScan
from .Item import Item, Color

class Rectangle(Item):
    __element__ = FigmaScan.Element(name="Rectangle", type="RECTANGLE")

    def __init__(self, js):
        Item.__init__(self, js)
        
        if "cornerRadius" in js:
            self.radius = js["cornerRadius"]
        else: self.radius = 1.0
        
        if "fills" in js:
            fills = js["fills"]
            if len(fills) > 0:
                self.color = Color(fills[0].get("color", {}))
