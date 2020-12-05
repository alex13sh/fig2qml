 
class Item:
    __figma_type__ = ""
    
    def __init__(self, js):
        if "absoluteBoundingBox" in js:
            pos = js["absoluteBoundingBox"]
            self.x = pos["x"]
            self.y = pos["y"]
            self.width = pos["width"]
            self.height = pos["height"]
