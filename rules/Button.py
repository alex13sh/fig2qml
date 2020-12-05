from . import FigmaScan
from .Item import Item

class Button(Item):
    __element__ = FigmaScan.Element(name="button", type=None)
    __can_children__ = False
    
    def __init__(self, js):
        Item.__init__(self, js)
        
        if "children" in js:
            childs = js["children"]
            elm = FigmaScan.get_element_by_path(childs, name=None, type="GROUP")
            #print("elm:", elm)
            if elm:
                elm = FigmaScan.get_element_by_path(elm.get("children"), name="Label", type="TEXT")
            if elm:
                self.text = elm.get("characters", None)
            
