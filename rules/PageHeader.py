from . import FigmaScan
from .Item import Item

class PageHeader(Item):
    __element__ = FigmaScan.Element(name="Header", type=None)
    __can_children__ = False

    def __init__(self, js):
        Item.__init__(self, js)
        
        if "children" in js:
            childs = js["children"]
            elm = FigmaScan.get_element_by_path(childs, name="Label", type="TEXT")
            if elm:
                self.title = elm.get("characters", None)
        
