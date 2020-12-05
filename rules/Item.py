import copy

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
    
    def get_qml(self):
        js =  copy.copy(self.__dict__)
        qml_type = self.__class__.__name__
        txt = qml_type + " {"
        del js["children"]
        
        def print_value(value):
            if type(value) is str:
                return f'"{value}"'
            elif type(value) is Color:
                (r, g, b, a) = value.get_tuple()
                return f'Qt.rgba({r}, {g}, {b}, {a})'
            else: return f'{value}'
            
        for prop, value in js.items():
            txt_line = f'{prop}: {print_value(value)}'
            txt += "\n\t" + txt_line
        for child in self.children:
            txt_child = "\n" + child.get_qml()
            txt_child = txt_child.replace("\n", "\n\t")
            txt += txt_child
        txt += "\n}"
        return txt
    
class Color:
    
    def __init__(self, js):
        self.r = js.get("r", 0)
        self.g = js.get("g", 0)
        self.b = js.get("b", 0)
        self.a = js.get("a", 1)
        
    def get_tuple(self):
        return (self.r, self.g, self.b, self.a)
