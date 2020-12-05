 
class Item:
    __figma_type__ = ""
    __can_children__ = True
    
    def __init__(self, js):
        if "absoluteBoundingBox" in js:
            pos = js["absoluteBoundingBox"]
            self.x = pos["x"]
            self.y = pos["y"]
            self.width = pos["width"]
            self.height = pos["height"]
            
    def get_js(self):
        js = self.__dict__
        js["type"] = self.__class__.__name__
        childs = []
        for child in self.children:
            childs.append(child.get_js())
        js["children"] = childs
        return js
